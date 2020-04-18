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


def lerp(v0, v1, i):
    return v0 + i * (v1 - v0)


def get_equidistant_points(p1, p2, n):
    return [[lerp(p1[0], p2[0], 1. / n * i), lerp(p1[1], p2[1], 1. / n * i)] for i in range(n)]


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def plot_flow_digraph(digraph, name="digraph.png"):
    g = nx.DiGraph()

    edges = digraph.get_edges()
    for e in edges:
        g.add_edge(e.get_tuple()[0], e.get_tuple()[1], weight=e.get_capacity())

    pos = {}
    x_offset = 0
    max_layer_size = max([len(layer) for layer in digraph.get_layers()])
    for layer in digraph.get_layers():
        points = get_equidistant_points((x_offset, 0), (x_offset, max_layer_size), len(layer))

        y_offset = 0
        if len(layer) < max_layer_size:
            y_offset = (max_layer_size - 1 - points[len(points) - 1][1]) / 2.0

        i = 0
        for node in layer:
            g.add_node(node.index)
            x, y = points[i]
            pos[node.index] = (x, y + y_offset)
            i += 1
        x_offset += 1

    nx.draw_networkx(g, pos)
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx(g, pos)
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
