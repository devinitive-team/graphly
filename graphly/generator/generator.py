import scipy.special
import random
from itertools import combinations
from operator import itemgetter

from graphly.graph import graph
from graphly.digraph import digraph
from graphly.representation import representation
from graphly.algorithm import algorithm


def generate(generation_type, *args):
    return {
        "normal": generate_regular,
        "probability": generate_probability,
        "probability-digraph": generate_probability_digraph,
        "k-regular": generate_k_regular,
        "eulerian": generate_eulerian,
        "random-connected": generate_random_connected,
        "degree-seq": generate_from_degree_seq,
        "strongly-connected-weighted-digraph": generate_strongly_connected_weighted_digraph
    }[generation_type](*args)


def generate_regular(vertices_num, edges_num):
    max_edges = int(scipy.special.binom(vertices_num, 2))
    if edges_num > max_edges:
        raise Exception("Too many edges")

    adj_list = [[] for _ in range(vertices_num)]
    i = 0
    while i < edges_num:
        edge = random.sample(range(vertices_num), 2)
        if edge[1] in adj_list[edge[0]]:
            continue
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

        i += 1

    return graph(representation.adjacency_list(adj_list))


def generate_probability(vertices_num, probability):
    if 0.0 > probability > 1.0:
        raise Exception("Probability domain [0, 1]")

    edge_list = list(combinations([i for i in range(vertices_num)], 2))

    adj_list = [[] for _ in range(vertices_num)]
    for i in range(len(edge_list)):
        if random.random() < probability:
            adj_list[edge_list[i][0]].append(edge_list[i][1])
            adj_list[edge_list[i][1]].append(edge_list[i][0])

    return graph(representation.adjacency_list(adj_list))


def generate_probability_digraph(vertices_num, probability):
    if 0.0 > probability > 1.0:
        raise Exception("Probability domain [0, 1]")

    edge_list = list(combinations([i for i in range(vertices_num)], 2))

    adj_list = [[] for _ in range(vertices_num)]
    for i in range(len(edge_list)):
        if random.random() < probability:
            adj_list[edge_list[i][0]].append(edge_list[i][1])
        if random.random() < probability:
            adj_list[edge_list[i][1]].append(edge_list[i][0])

    return digraph(representation.adjacency_list(adj_list, is_directed=True))


def generate_k_regular(n, k):  # n - number of vertices, k - regularity
    # number of number * regularity must be even and regularity cannot be larger than number of vertices
    if n * k % 2 != 0 or k >= n:
        raise Exception("Wrong input numbers")

    nk = n * k

    adj_list = [[] for _ in range(n)]
    points_org = [i % n for i in range(nk)]
    points = points_org[:]
    edge_list = []

    response = 0

    while True:
        for i in range(nk // 2):
            response = generate_random_pair(edge_list, points)  # 0 is ok, -1 is not ok
            if response == -1:  # if response == -1 generating graph again
                break
        if response == 0:  # if response == 0 graph is finished
            break

        # resetting
        edge_list = []
        points = points_org[:]

    for i in range(len(edge_list)):  # transform from list of edges to adjacency list
        adj_list[edge_list[i][0]].append(edge_list[i][1])
        adj_list[edge_list[i][1]].append(edge_list[i][0])

    return graph(representation.adjacency_list(adj_list))


def generate_random_pair(edge_list, points):
    loop_count = 0
    point = points.pop(random.randrange(len(points)))

    while True:
        if loop_count > 10:  # to prevent inf loop
            return -1
        loop_count += 1

        index = random.randrange(len(points))

        if point == points[index]:
            continue

        edge = (point, points[index])
        if edge in edge_list:
            continue

        reversed_edge_list = [t[::-1] for t in edge_list]
        if edge in reversed_edge_list:
            continue

        points.pop(index)
        edge_list.append(edge)
        return 0


def generate_eulerian(vertices_num=random.randint(4, 50)):
    """
    :param vertices_num or nothing
    :return: an eulerian graph
    """
    max_degree = vertices_num - 2 if vertices_num % 2 == 0 else vertices_num - 1

    seq = None
    is_degree_seq = False
    while not is_degree_seq:
        seq = []
        for vertex in range(vertices_num):
            seq.append(random.randrange(2, max_degree + 1, 2))  # all vertices of even degree

        is_degree_seq = algorithm.is_degree_seq(seq)

    g = generate("degree-seq", seq)

    return g


def generate_random_connected(vertices_num):
    while True:
        g = generate_probability(vertices_num, 0.3)
        if algorithm.is_connected(g):
            return g


def generate_from_degree_seq(sequence):
    if not algorithm.is_degree_seq(sequence):
        raise Exception("Provide a sequence that is a degree sequence.")

    seq = [[index, value] for index, value in enumerate(sequence)]

    adj_list = [[] for _ in range(len(seq))]
    for _ in range(len(seq)):
        seq.sort(reverse=True, key=itemgetter(1))
        i = 0
        j = i + 1
        while seq[i][1] > 0 and j < len(seq):
            adj_list[seq[i][0]].append(seq[j][0])
            adj_list[seq[j][0]].append(seq[i][0])
            seq[i][1] -= 1
            seq[j][1] -= 1
            j += 1

    return graph(representation.adjacency_list(adj_list))


def generate_strongly_connected_weighted_digraph(vertices_num, probability, weight_min, weight_max):
    di_g = generate("probability-digraph", vertices_num, probability)

    while len(set(algorithm.kosaraju_algorithm(di_g))) > 1:  # check if all numbers in array are the same
        di_g = generate("probability-digraph", vertices_num, probability)

    for e in di_g.get_edges():
        e.set_weight(random.randint(weight_min, weight_max))

    return di_g
