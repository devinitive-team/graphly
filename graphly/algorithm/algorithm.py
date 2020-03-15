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


def components_helper(nr, v, G, comp):
    vert = G.nodes()
    for n in vert:
        if comp[n] == -1:
            comp[n] = nr
            components_helper(nr, n, G, comp)


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
