# graph_logic.py

import networkx as nx
from data2 import halte

# =========================
# MEMBUAT GRAPH
# =========================
def create_graph():
    G = nx.Graph()

    for asal in halte:
        for tujuan, jarak in halte[asal].items():
            G.add_edge(
                asal,
                tujuan,
                weight=jarak
            )

    return G

# =========================
# CARI RUTE TERPENDEK
# =========================
def shortest_path(graph, start, end):

    path = nx.shortest_path(
        graph,
        source=start,
        target=end,
        weight='weight'
    )

    distance = nx.shortest_path_length(
        graph,
        source=start,
        target=end,
        weight='weight'
    )

    return path, round(distance, 2)