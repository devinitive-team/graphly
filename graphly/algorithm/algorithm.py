import random
import itertools


def is_degree_seq(sequence):
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
    vert = graph.nodes()
    for u in vert:
        if graph.edge_exists(u, v):
            if comp[u] == -1:
                comp[u] = nr
                components_helper(nr, u, graph, comp)


def components(graph):
    nr = 0
    vert = graph.nodes()
    comp = [-1 for v in vert]
    for v in vert:
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_helper(nr, v, graph, comp)
    return comp


def largest_component(graph):
    component_array = components(graph)
    num_of_components = max(component_array)

    for i in range(1, num_of_components + 1):
        print(f"{i}) ", end='')
        for index, value in enumerate(component_array):
            if i == value:
                print(f"{index} ", end='')
        print()

    counted_components = dict((comp, component_array.count(comp)) for comp in component_array)
    largest = max(counted_components, key=counted_components.get)
    print(f"Largest component: {largest}")


def randomize_graph(graph, num):
    for _ in range(num):
        edges = graph.edges()
        random_edges = random.choices(edges, k=2)
        ready = False
        while not ready:
            for node in random_edges[0]:
                if node in random_edges[1]:
                    random_edges = random.choices(edges, k=2)
                    ready = False
                    break
                else:
                    ready = True

        graph.exchange_edges(random_edges)


def is_hamiltonian(graph):
    nodes = graph.nodes()
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
