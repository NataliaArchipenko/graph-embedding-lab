# Graph Embedding & Network Analysis Project

Dieses Projekt demonstriert die Erstellung, Analyse und Einbettung von Graphen mit modernen Graph-Embedding-Methoden wie **Node2Vec** und **DeepWalk**.  
Zusätzlich werden echte Daten verarbeitet, Ähnlichkeiten berechnet, Anomalien erkannt und Graphdaten in RDF konvertiert.

**Repository-Struktur:**
- Aufbau eines Wikipedia-Graphen  
- DeepWalk / Node2Vec Embeddings  
- Ähnlichkeitsanalyse  
- Anomalieerkennung in Finanztransaktionen  
- Export nach RDF (Turtle)
- Visualisierung in 2D & 3D

**Projektstruktur:**
GraphEmbedding:
- README.md
- data:
     - edges.csv
     - embedding.csv
     - graph_edges.csv
     - FullData.csv
     - FullData_1.csv
     - wiki_graph.ttl
     - wiki_graph_f.ttl
     - wiki_graph_fixed.ttl
- notebooks
     - 01_build_wikipedia_graph.ipynb
     - 02_node2vec_deepwalk_embeddings.ipynb
     - 03_similarity_analysis.ipynb
     - graph_em_tutor.ipynb
- model
     - trained_model.pkl
     - model
-scripts
     - datei_create.py
     - test.py
     - test_stream.py
     - 
## 1. Wikipedia Knowledge Graph

Erstellt einen Graphen aus Wikipedia-Artikeln zum Thema Künstliche Intelligenz:
- Artikel abrufen
- interne Links extrahieren
- Graph mit NetworkX erzeugen
- Visualisierung (2D)

**Notebook:** notebooks/01_build_wikipedia_graph.ipynb

## 2. DeepWalk / Node2Vec Embeddings

Erzeugt Graph-Einbettungen:
- Random Walks
- DeepWalk-Modell
- Embedding-Matrix
- 2D & 3D Streudiagramm

**Notebook:** notebooks/02_node2vec_deepwalk_embeddings.ipynb

## 3. Ähnlichkeitsanalyse

Berechnet Ähnlichkeiten zwischen Wikipedia-Artikeln:
- Cosine Similarity Matrix
- Top-5 ähnliche Artikel
- Visualisierung in 3D

**Notebook:** notebooks/03_similarity_analysis.ipynb

## 4. RDF-Export
Konvertiert Graphdaten in RDF/Turtle-Format:
- wiki_graph.ttl
- wiki_graph_fixed.ttl

## 5. Installation

pip install -r requirements.txt
## 6. Ausführen

- Repository klonen:
    git clone https://github.com/USERNAME/GraphEmbedding.git
    cd GraphEmbedding
  - Notebook starten:
    jupyter notebook
## 7 Ergebnisse
  - Vollständiger Wikipedia-Graph
  - DeepWalk / Node2Vec Embeddings
  - 2D & 3D Visualisierungen
  - Ähnlichkeitsanalyse
  - RDF-Export

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
