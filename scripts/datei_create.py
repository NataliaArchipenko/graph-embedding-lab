'''import networkx as nx
import matplotlib.pyplot as plt
import csv

# Kantenliste definieren
edges = [
    (1, 2), (1, 3), (1, 4), (1, 18), (1, 20), (1, 22),
    (2, 3), (2, 8), (3, 9), (3, 14), (4, 8), (4, 13),
    (5, 6), (5, 11), (6, 7), (6, 17), (7, 17),
    (9, 10), (9, 14), (9, 20), (10, 16), (10, 23),
    (12, 18), (13, 31), (14, 29), (15, 21), (15, 27),
    (16, 23), (19, 21), (24, 26), (25, 26), (28, 32),
    (30, 34), (31, 33), (32, 33), (33, 34)
]

# Datei speichern als CSV
file_path = "graph_edges.csv"
with open(file_path, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Source", "Target"])  # Spaltenüberschriften
    writer.writerows(edges)

print(f"Datei '{file_path}' wurde erfolgreich erstellt.")'''

import csv
import random
import networkx as nx
import matplotlib.pyplot as plt

# Beispiel-Spielerdaten mit den gewünschten Spalten
players = [
    ["Lionel Messi", "Inter Miami", "Forward", 93],
    ["Lue  Meki", "Inter Miami", "Forward", 90],
    ["Cristiano Ronaldo", "Al-Nassr", "Forward", 92],
    ["Kylian Mbappé", "PSG", "Forward", 91],
    ["Erling Haaland", "Man City", "Forward", 90],
    ["Kevin De Bruyne", "Man City", "Midfielder", 91],
    ["Robert Lewandowski", "Barcelona", "Forward", 91],
    ["Neymar Jr.", "Al-Hilal", "Forward", 89],
    ["Mohamed Salah", "Liverpool", "Forward", 89],
    ["Luka Modrić", "Real Madrid", "Midfielder", 88],
    ["Toni Kroos", "Real Madrid", "Midfielder", 88],
    ["Virgil van Dijk", "Liverpool", "Defender", 88],
    ["Casemiro", "Man United", "Midfielder", 87],
    ["Bruno Fernandes", "Man United", "Midfielder", 87],
    ["Harry Kane", "Bayern Munich", "Forward", 90],
    ["Karim Benzema", "Al-Ittihad", "Forward", 91],
    ["Pedri", "Barcelona", "Midfielder", 85],
    ["Jude Bellingham", "Real Madrid", "Midfielder", 86],
    ["Vinícius Jr.", "Real Madrid", "Forward", 89],
    ["Son Heung-min", "Tottenham", "Forward", 88],
    ["Joshua Kimmich", "Bayern Munich", "Midfielder", 88],
]

# Datei speichern als CSV
file_path = "FullData.csv"
with open(file_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Club", "Club_Position", "Rating"])  # Spaltenüberschriften
    writer.writerows(players)

print(f"Datei '{file_path}' wurde erfolgreich erstellt.")
