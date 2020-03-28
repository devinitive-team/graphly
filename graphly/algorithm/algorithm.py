import random
import itertools
import copy


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
