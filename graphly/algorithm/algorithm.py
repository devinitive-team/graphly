import random
import itertools
import copy
import math
import copy

import numpy as np

from collections import defaultdict
from graphly.graph import graph
from graphly.digraph import digraph
from graphly.flow_graph import flow_graph
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
    graph_copy.remove_edge_by_index(edge)
    return not is_connected(graph_copy)


def remove_edge(g_dict, u, v):
    for index, key in enumerate(g_dict[u]):
        if key == v:
            g_dict[u].pop(index)
    for index, key in enumerate(g_dict[v]):
        if key == u:
            g_dict[v].pop(index)


def dfs_count(v, visited, g_dict):
    count = 1
    visited[v] = True
    for i in g_dict[v]:
        if not visited[i]:
            count = count + dfs_count(i, visited, g_dict)
    return count


def is_valid_next_edge(u, v, g_dict, vertices_num):
    if len(g_dict[u]) == 1:
        return True
    else:
        visited = [False] * vertices_num
        count1 = dfs_count(u, visited, g_dict)

        remove_edge(g_dict, u, v)

        visited = [False] * vertices_num
        count2 = dfs_count(u, visited, g_dict)

        g_dict[u].append(v)
        g_dict[v].append(u)

    return False if count1 > count2 else True


def print_euler_node(u, g_dict, vertices_num):
    for v in g_dict[u]:
        if is_valid_next_edge(u, v, g_dict, vertices_num):
            print("%d-%d " % (u, v))
            remove_edge(g_dict, u, v)
            print_euler_node(v, g_dict, vertices_num)


def find_eulerian_circuit(g):
    """
    :param g graph
    :return: eulerian circuit as an array of integers
    """
    if not is_eulerian(g):
        raise Exception

    g_dict = defaultdict(list)
    for e in g.get_edges():
        u, v = e.get_tuple()
        g_dict[u].append(v)
        g_dict[v].append(u)

    u = 0

    print_euler_node(u, g_dict, len(g.get_nodes()))


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
    return distances.index(min(distances))  # index of min value in list


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
            weight = e.get_weight()
            if d_s[v] > d_s[u] + weight:
                d_s[v] = d_s[u] + weight
                p_s[v] = u

    for e in g.get_edges():
        u, v = e.get_tuple()
        weight = e.get_weight()
        if d_s[v] > d_s[u] + weight:
            return False, d_s

    return True, d_s


def johnson_algorithm(g):
    new_g, new_node = add_s(g)
    copy_weights(g, new_g)

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


def ford_fulkerson(g, s, t):
    for e in g.get_edges():
        e.set_flow(0)

    gf = generate_gf(g)

    path = bfs(gf, s)
    while path:
        c_f = min([e.get_residual_capacity() for e in path])
        for i in range(len(path)):
            try:
                u, v = path[i].get_tuple()
                edg = g.get_edge(u, v)
                edg.set_flow(edg.get_flow() + c_f)
            except:
                u, v = path[i].get_tuple()
                edg = g.get_edge(v, u)
                edg.set_flow(edg.get_flow() - c_f)

        gf = generate_gf(g)
        path = bfs(gf, s)

    return g


def bfs(g, s):
    d_s = [math.inf for _ in range(len(g.get_nodes()))]
    p_s = [None for _ in range(len(g.get_nodes()))]

    d_s[s] = 0

    Q = [s]
    while Q:
        v = Q.pop()
        neighbours = [n.edge_tuple[1] for n in list(filter(lambda x: x.edge_tuple[0] == v, g.get_edges()))]
        for u in neighbours:
            if d_s[u] == math.inf:
                d_s[u] = d_s[v] + 1
                p_s[u] = v
                Q.append(u)

    if p_s[1] is None:
        return None

    path = [(p_s[1], 1)]
    while path[-1][0] != 0:
        path.append((p_s[p_s[path[-1][1]]], p_s[path[-1][1]]))

    path.reverse()
    return [g.get_edge(*e) for e in path]


def generate_gf(g):
    gf = copy.deepcopy(g)
    edges_copy = copy.deepcopy(gf.get_edges())
    for e in edges_copy:
        residual_capacity = e.get_capacity() - e.get_flow()
        if residual_capacity > 0:
            gf.get_edge(*e.get_tuple()).set_residual_capacity(residual_capacity)

    for e in gf.get_edges():
        if e.get_residual_capacity() == 0:
            gf.remove_edge(e)

    for e in gf.get_edges():
        if e.get_residual_capacity() == 0:
            gf.remove_edge(e)

    for e in gf.get_edges():
        if e.get_residual_capacity() == 0:
            gf.remove_edge(e)

    return gf


def pagerank_iterative(M, num_iterations: int = 100, d: float = 0.15):
    N = M.shape[1]
    v = np.ones(N)
    v = v / np.linalg.norm(v, 1)
    M_hat = ((1 - d) * M + d / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v


def pagerank_surfer(M, num_iterations: int = 100, d: float = 0.15):
    N = M.shape[1]
    v = np.zeros(N)
    current_node = random.randint(0, N - 1)
    for i in range(num_iterations):
        v[current_node] += 1
        if random.random() < (1 - d):
            next_nodes = np.array([], dtype=int)
            for index, el in enumerate(M[:, current_node]):
                if el != 0:
                    next_nodes = np.append(next_nodes, np.int32(index))
            current_node = np.random.choice(a=next_nodes, size=1)[0]
        else:
            current_node = random.randint(0, N - 1)

    return v / num_iterations
