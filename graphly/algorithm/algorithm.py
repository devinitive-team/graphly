import random
import itertools
import copy
import math

from graphly.graph import graph
from graphly.digraph import digraph
from graphly.representation import representation
from graphly.edge import edge


def is_degree_seq(sequence):
    """
    :param sequence: sequence as an array of integers
    :return: boolean
    """
    seq = sequence.copy()

    seq.sort(reverse=True)
    while True:
        if all(v == 0 for v in seq):
            return True

        if seq[0] < 0 or seq[0] >= len(seq):
            return False

        for i in range(1, seq[0] + 1):
            seq[i] -= 1
            if seq[i] < 0:
                return False

        seq[0] = 0
        seq.sort(reverse=True)


def components_helper(nr, v, graph, comp):
    vert = graph.get_nodes()
    for u in vert:
        if graph.edge_exists(u, v):
            if comp[u] == -1:
                comp[u] = nr
                components_helper(nr, u, graph, comp)


def components(graph):
    """
    :param graph
    :return: array of integers ordered that every vertex belongs to a component
    """
    nr = 0  # which connected component
    vert = graph.get_nodes()
    comp = [-1 for _ in vert]  # no vertices were visited
    for v in vert:
        if comp[v] == -1:
            nr += 1
            comp[v] = nr  # mark v as visited and belongs to 'nr' component
            components_helper(nr, v, graph, comp)
    return comp


def largest_component(graph):
    """
    :param graph
    :return: a dictionary of vertices grouped in components,
             a number which component is the largest
    """
    component_array = components(graph)
    num_of_components = max(component_array)
    components_dict = {}

    for i in range(1, num_of_components + 1):
        components_dict[i] = []
        for index, value in enumerate(component_array):
            if i == value:
                components_dict[i].append(index)

    counted_components = dict((comp, component_array.count(comp)) for comp in component_array)
    largest = max(counted_components, key=counted_components.get)
    return components_dict, largest


def randomize_graph(graph, num):
    """
    :param graph
    :param num: number of randomizations
    """
    for _ in range(num):
        edges = graph.get_edges()
        random_edges = random.choices(edges, k=2)
        ready = False
        while not ready:
            for node in random_edges[0].get_tuple():
                if node in random_edges[1].get_tuple():
                    random_edges = random.choices(edges, k=2)
                    ready = False
                    break
                else:
                    ready = True

        graph.exchange_edges([e.get_tuple() for e in random_edges])


def is_hamiltonian(graph):
    nodes = graph.get_nodes()
    permutations = list(itertools.permutations(nodes))

    graph.set_representation("adjacency_matrix")

    for permutation in permutations:
        valid = True
        for i in range(len(permutation)):
            if not graph.edge_exists(permutation[i], permutation[(i + 1) % len(permutation)]):
                valid = False
                break

        if valid:
            return True

    return False


def is_connected(graph):
    """
    :param graph
    :return: bool
    """
    component_array = components(graph)
    return max(component_array) == 1


def is_eulerian(graph):
    """
    Graph is eulerian when graph is connected and all its vertices are of even degree.
    :param graph
    :return: bool
    """
    graph.set_representation("adjacency_list")
    vertices_degree = []
    for vertex in graph.get_vertices():
        vertices_degree.append(len(vertex))

    is_every_degree_even = all(degree % 2 == 0 for degree in vertices_degree)
    return is_connected(graph) and is_every_degree_even


def is_edge_bridge(graph, edge):
    """
    :param graph
    :param edge
    :return: bool
    """
    if not is_connected(graph):
        raise Exception

    graph_copy = copy.deepcopy(graph)
    graph_copy.remove_edge(edge)
    return not is_connected(graph_copy)


def find_eulerian_circuit(graph):
    """
    :param graph
    :return: eulerian circuit as an array of integers
    """
    if not is_eulerian(graph):
        raise Exception

    graph.set_representation("adjacency_list")

    edge_count = dict()

    for i in range(len(graph.get_vertices())):
        edge_count[i] = len(graph.get_vertices()[i])

    eulerian_circuit = []
    current_path = []
    current_vertex = 0
    current_path.append(current_vertex)

    while len(current_path):
        if edge_count[current_vertex]:
            next_vertex = graph.get_vertices()[current_vertex][-1]

            edge_count[current_vertex] -= 1
            graph.get_vertices()[current_vertex].pop()

            current_vertex = next_vertex

            current_path.append(current_vertex)
        else:
            eulerian_circuit.append(current_vertex)
            current_vertex = current_path[-1]
            current_path.pop()

    eulerian_circuit.reverse()
    return eulerian_circuit


def minimum_distance(g, d_s, S):
    """ Dijkstra algorithm helper function """
    vertex_count = len(g.get_vertices())

    minimum = math.inf
    minimum_index = None

    for v in range(vertex_count):
        if d_s[v] < minimum and v not in S:
            minimum = d_s[v]
            minimum_index = v

    return minimum_index


def dijkstra_algorithm(g, source=0):
    """
    :param g: weighted graph
    :param source: a vertex which execution of algorithm is started, defaulted to 0
    :return array of shortest paths from  given vertex
    """
    vertex_count = len(g.get_vertices())
    d_s = [math.inf for _ in range(vertex_count)]
    d_s[source] = 0
    p_s = [None for _ in range(vertex_count)]

    S = []
    while sorted(S) != list(range(vertex_count)):
        u = minimum_distance(g, d_s, S)
        S.append(u)

        for v in g.get_vertices()[u]:
            if v not in S:
                weight = g.get_edge(u, v).get_weight()
                if d_s[v] > d_s[u] + weight:
                    d_s[v] = d_s[u] + weight
                    p_s[v] = u

    return d_s


def prim_algorithm(g):
    n_in_graph = g.get_nodes()
    n_in_tree = []
    e = g.get_edges()
    T = [[] for _ in range(len(n_in_graph))]
    n_in_tree.append(n_in_graph[0])
    while len(n_in_tree) != len(n_in_graph):
        current_edges = list(
            filter(lambda x: x.edge_tuple[0] in n_in_tree and x.edge_tuple[1] not in n_in_tree, e)) + list(
            filter(lambda x: x.edge_tuple[0] not in n_in_tree and x.edge_tuple[1] in n_in_tree, e))
        current_edges.sort(key=lambda x: x.weight, reverse=False)
        n_in_tree.append(current_edges[0].edge_tuple[1] if current_edges[0].edge_tuple[0] in n_in_tree else
                         current_edges[0].edge_tuple[0])
        T[current_edges[0].edge_tuple[0]].append(current_edges[0].edge_tuple[1])
        T[current_edges[0].edge_tuple[1]].append(current_edges[0].edge_tuple[0])
    result = graph(representation.adjacency_list(T))
    result_e = result.get_edges()
    for res_e in result_e:
        for src_e in e:
            if res_e.edge_tuple[0] == src_e.edge_tuple[0] and res_e.edge_tuple[1] == src_e.edge_tuple[1]:
                res_e.set_weight(src_e.get_weight())
    return result


def calculate_distance_matrix(g):
    matrix = []

    for v in range(len(g.get_vertices())):
        matrix.append(dijkstra_algorithm(g, v))

    return matrix


def calculate_center(g):
    """
    :param g: graph
    :return: index of center vertex in given graph
    """
    distance_matrix = calculate_distance_matrix(g)
    distances = list(map(sum, zip(*distance_matrix)))  # sum of columns
    return distances.index(max(distances))  # index of max value in list


def calculate_minmax_center(g):
    """
    :param g: graph
    :return: index of minmax center vertex in given graph
    """
    distance_matrix = calculate_distance_matrix(g)
    max_distances = list(map(max, zip(*distance_matrix)))  # max value in each column
    return max_distances.index(min(max_distances))  # index of min value in list


def DFS_visit(v, g, d, f, t):
    t = t + 1
    d[v] = t

    neighbours = [n.edge_tuple[1] for n in list(filter(lambda x: x.edge_tuple[0] == v, g.get_edges()))]
    for n in neighbours:
        if d[n] == -1:
            t = DFS_visit(n, g, d, f, t)

    t = t + 1
    f[v] = t
    return t


def components_r(nr, v, gT, comp):
    neighbours = [n[1] for n in list(filter(lambda x: x[0] == v, gT))]
    for n in neighbours:
        if comp[n] == -1:
            comp[n] = nr
            components_r(nr, v, gT, comp)


def kosaraju_algorithm(g):
    # when all numbers in returned array are the same, digraph is strongly connected
    vert = g.get_nodes()
    d = [-1 for _ in range(len(vert))]
    f = [-1 for _ in range(len(vert))]
    t = 0
    for v in vert:
        if d[v] == -1:
            t = DFS_visit(v, g, d, f, t)

    gT = g.transpose_edges()
    f = [(c, val) for c, val in enumerate(f, 0)]
    f.sort(key=lambda x: x[1], reverse=True)
    nr = 0
    comp = [-1 for _ in range(len(vert))]
    for elem in f:
        v = elem[0]
        if comp[v] == -1:
            nr = nr + 1
            comp[v] = nr
            components_r(nr, v, gT, comp)
    return comp


def bellman_ford_algorithm(g, source=0):
    """
    :param g: strongly connected weighted digraph
    :param source: a vertex which execution of algorithm is started, defaulted to 0
    :return: bool
    """
    vertex_count = len(g.get_vertices())
    d_s = [math.inf for _ in range(vertex_count)]
    d_s[source] = 0
    p_s = [None for _ in range(vertex_count)]

    for _ in range(vertex_count - 1):
        for e in g.get_edges():
            u, v = e.get_tuple()
            weight = g.get_edge(u, v).get_weight()
            if d_s[v] > d_s[u] + weight:
                d_s[v] = d_s[u] + weight
                p_s[v] = u

    for e in g.get_edges():
        u, v = e.get_tuple()
        weight = g.get_edge(u, v).get_weight()
        if d_s[v] > d_s[u] + weight:
            return False, d_s

    return True, d_s


def johnson_algorithm(g):
    new_g, new_node = add_s(g)
    copy_weights(g, new_g)
    new_g.plot_weighted("new_g.png")
    g.plot_weighted("g.png")

    is_valid, d_s = bellman_ford_algorithm(new_g, new_node)
    if not is_valid:
        raise Exception("Istnieje cykl o ujemnej wadze!")

    h = [0 for _ in range(new_node + 1)]
    for v in new_g.get_nodes():
        h[v] = d_s[v]

    for e in new_g.get_edges():
        u, v = e.get_tuple()
        e.set_weight(e.get_weight() + h[u] - h[v])

    copy_weights(new_g, g)

    D = [[] for _ in g.get_nodes()]
    for u in g.get_nodes():
        D[u].extend(0 for _ in g.get_nodes())
        d_u = dijkstra_algorithm(g, u)
        print(d_u)
        print(u, v)
        print(h)
        for v in g.get_nodes():
            D[u][v] = d_u[v] - h[u] + h[v]

    return D


def add_s(g):
    new_g = g.copy()

    new_node = len(g.get_nodes())
    new_g.get_nodes().append(new_node)
    new_g.get_vertices().append([])

    for node in new_g.get_nodes():
        if node == new_node:
            continue
        new_g.get_edges().append(edge((new_node, node), 0))
        new_g.get_vertices()[new_node].append(node)

    return new_g, new_node


def copy_weights(g_from, g_to):
    for e in g_to.get_edges():
        u, v = e.get_tuple()
        try:
            e.set_weight(g_from.get_edge(u, v).get_weight())
        except:
            pass
