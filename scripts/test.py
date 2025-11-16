import networkx as nx
import wikipediaapi
import numpy as np
import matplotlib.pyplot as plt
from karateclub.node_embedding.neighbourhood import DeepWalk
from sklearn.metrics.pairwise import cosine_similarity
from rdflib import Graph, Namespace, URIRef

# Wikipedia-API initialisieren mit User-Agent
wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="MyKIProject/1.0 (mailto:your-email@example.com)"
)

# Liste der Wikipedia-Artikel zum Thema KI
articles = [
    "Artificial intelligence", "Machine learning", "Deep learning", "Neural network",
    "Computer vision", "Natural language processing", "Reinforcement learning",
    "Expert system", "Turing test", "Supervised learning"
]

# Graph erstellen
G = nx.Graph()

# Artikel und Verlinkungen hinzufügen
for article in articles:
    page = wiki.page(article)
    if not page.exists():
        continue
    G.add_node(article)
    for link in page.links:
        if link in articles:  # Nur interne Links innerhalb unserer Artikel nutzen
            G.add_edge(article, link)

# Temporär numerische IDs für DeepWalk erzeugen
node_mapping = {node: i for i, node in enumerate(G.nodes())}
G_numeric = nx.relabel_nodes(G, node_mapping)

# DeepWalk für Node Embeddings (mit numerischen IDs)
deepwalk = DeepWalk(dimensions=3)
deepwalk.fit(G_numeric)
embedding = deepwalk.get_embedding()

# Ähnlichkeit berechnen
similarity_matrix = cosine_similarity(embedding)

# Ähnlichste Artikel ausgeben
article_indices = {i: articles[i] for i in range(len(articles))}
print("\nÄhnliche Wikipedia-Artikel zu 'Artificial intelligence':")
ai_index = articles.index("Artificial intelligence")
similarities = list(enumerate(similarity_matrix[ai_index]))
similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
for i, score in similarities[1:6]:  # Die 5 ähnlichsten Artikel
    print(f"{article_indices[i]} (Score: {score:.4f})")

# RDF Namespace
EX = Namespace("http://example.org/")

# RDF-Graph neu erstellen
rdf_graph = Graph()

# Knoten und Kanten hinzufügen
for node in G.nodes():
    node_name = node.replace(" ", "_")  # Leerzeichen durch Unterstriche ersetzen
    rdf_graph.add((URIRef(EX[node_name]), EX.wikitype, EX.wikiArticle))  

for edge in G.edges():
    source = edge[0].replace(" ", "_")
    target = edge[1].replace(" ", "_")
    rdf_graph.add((URIRef(EX[source]), EX.wikilinksTo, URIRef(EX[target])))  

# Speichern als Turtle-Datei
rdf_graph.serialize("wiki_graph_fixed.ttl", format="turtle")
print("Graph wurde als 'wiki_graph_fixed.ttl' gespeichert!")

