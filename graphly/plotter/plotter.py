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


def plot_digraph(digraph, name="digraph.png"):
    g = nx.DiGraph()

    for node in digraph.get_nodes():
        g.add_node(node)

    edges = digraph.get_edges()
    for e in edges:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1])

    nx.draw_circular(g, with_labels=True)

    plt.savefig(name, format="png")
    plt.clf()


def plot_weighted_digraph(digraph, name="digraph.png"):
    g = nx.DiGraph()

    for node in digraph.get_nodes():
        g.add_node(node)

    edges = digraph.get_edges()
    for e in edges:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1], weight=e.get_weight())

    pos = nx.circular_layout(g)
    nx.draw_networkx(g, pos)
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.savefig(name, format="png")
    plt.clf()


def plot_flow_digraph(digraph, name="digraph.png"):
    g = nx.DiGraph()

    for node in digraph.get_nodes():
        g.add_node(node)

    edges = digraph.get_edges()
    for e in edges:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1], weight=e.get_capacity())

    pos = nx.circular_layout(g)
    nx.draw_networkx(g, pos)
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.savefig(name, format="png")
    plt.clf()


def plot_with_component(digraph, components, name="digraph.png"):
    plt.clf()
    g = nx.DiGraph()
    colors = []
    colors_map = ['red', 'orange', 'yellow', 'brown', 'green', 'blue', 'pink', 'purple']
    if max(components) > len(colors_map):
        raise Exception("Not enough colors to draw graph")
    for node in digraph.get_nodes():
        g.add_node(node)
        colors.append(colors_map[components[node]])

    edges = digraph.get_edges()
    for e in edges:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1], weight=e.get_weight(), color='red')
    pos = nx.circular_layout(g)
    nx.draw_networkx(g, pos, node_color=colors)
    plt.savefig(name, format="png")
    plt.clf()
