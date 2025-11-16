import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import wikipediaapi

st.title("KI-Netzwerk Analyse")

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

# Graph visualisieren
fig, ax = plt.subplots(figsize=(10, 7))  # Eine explizite Figure erstellen
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1000, font_size=10, ax=ax)

# Visualisierung in Streamlit anzeigen
st.pyplot(fig)  # Die explizite Figur weitergeben
