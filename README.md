# Graph Embedding & Network Analysis
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![NetworkX](https://img.shields.io/badge/Graph-NetworkX-3776AB)
![DeepWalk](https://img.shields.io/badge/Embedding-DeepWalk-ff69b4)
![Node2Vec](https://img.shields.io/badge/Embedding-Node2Vec-009688)
> Graph Embeddings & Wikipedia Knowledge Graph – Lern- und Experimentierprojekt

Dieses Projekt demonstriert die Erstellung, Analyse und Einbettung von Graphen mit modernen Graph-Embedding-Methoden wie **Node2Vec** und **DeepWalk**.  
Als Beispiel dienen **Wikipedia-Artikel aus dem Themenbereich Künstliche Intelligenz** sowie **synthetisch erzeugte Graph-Beispieldaten**.

Das Projekt umfasst:

- Aufbau eines Wikipedia-Graphen  
- Generierung von Node2Vec / DeepWalk Embeddings  
- Ähnlichkeitsanalyse zwischen Artikeln  
- 2D- & 3D-Visualisierung  
- Export der Graphdaten nach RDF/Turtle  
- Zusätzliche Beispielskripte für Graphgenerierung  

Es handelt sich **ausschließlich um Trainings- und Experimentierdaten**, keine realen Finanz- oder sensiblen Daten.

**Projektstruktur:**
GraphEmbedding:
- README.md
- LICENSE
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
**Notebook:** notebooks/01_build_wikipedia_graph.ipynb
Funktionen:
- Abruf von Wikipedia-Artikeln  
- Extraktion interner Links  
- Aufbau eines gerichteten Graphen mit NetworkX  
- Grundvisualisierung des Graphen 

## 2. DeepWalk / Node2Vec Embeddings
**Notebook:** notebooks/02_node2vec_deepwalk_embeddings.ipynb
Beinhaltet:
- Random Walk Generierung  
- DeepWalk-Training  
- Embedding-Matrix  
- Visualisierung in 2D und 3D  

## 3. Ähnlichkeitsanalyse
**Notebook:** notebooks/03_similarity_analysis.ipynb
Features:
- Cosine Similarity Berechnung  
- Top-k ähnliche Wikipedia-Artikel  
- 3D-Plot der Embeddings 



## 4. RDF-Export
Das Projekt ermöglicht die Konvertierung der Graphdaten in das **RDF/Turtle-Format**.
- `wiki_graph.ttl`  
- `wiki_graph_f.ttl`  
- `wiki_graph_fixed.ttl`
  
## 5. Skripte
Unter `/scripts/` befinden sich zusätzliche Demonstrationsdateien:
- `datei_create.py` → erzeugt CSV-Dateien aus Beispiel-Graphen  
- `test.py` / `test_stream.py` → kleine Testskripte 

##  Installation

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
  - Ähnlichkeitsanalyse
  - 2D & 3D Visualisierungen
  - RDF-Export
## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
Verwendete Daten sind rein synthetisch oder stammen aus öffentlich zugänglichen Wikipedia-Artikeln.

