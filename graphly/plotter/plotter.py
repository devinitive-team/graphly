from operator import attrgetter
import networkx as nx
import matplotlib.pyplot as plt


def plot(graph, name="graph.png"):
    g = nx.Graph()

    for node in graph.get_nodes():
        g.add_node(node)

    temp = graph.get_edges()
    temp.sort(key=attrgetter("edge_tuple"))
    for e in temp:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1])

    nx.draw_circular(g, with_labels=True)

    plt.savefig(name, format="png")
    plt.clf()


def plot_weighted(graph, name="graph.pnt"):
    g = nx.Graph()

    for node in graph.get_nodes():
        g.add_node(node)

    temp = graph.get_edges()
    temp.sort(key=attrgetter("edge_tuple"))
    for e in temp:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1], weight=e.get_weight())

    pos = nx.circular_layout(g)
    nx.draw_networkx(g, pos)
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.savefig(name, format="png")
    plt.clf()
