import networkx as nx
import matplotlib.pyplot as plt


def plot(graph, name="graph.png"):
    g = nx.Graph()

    for node in graph.nodes():
        g.add_node(node)

    temp = graph.edges()
    temp.sort()
    for edge in temp:
        g.add_edge(edge[0], edge[1])

    print(g.nodes())
    print(g.edges())

    nx.draw_circular(g, with_labels=True)
    plt.savefig(name)
