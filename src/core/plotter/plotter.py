import networkx as nx
import matplotlib.pyplot as plt


def plot(graph):
    g = nx.Graph()

    for edge in graph.edges():
        g.add_edge(edge[0], edge[1])

    nx.draw_shell(g, with_labels=True)
    plt.savefig("filename.png")
