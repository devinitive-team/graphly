import scipy.special
import random
from itertools import combinations

from graphly.graph import graph
from graphly.representation.representation import adjacency_list


def generate(generation_type, x, y):
    return {
        "normal": generate_regular,
        "probability": generate_probability
    }[generation_type](x, y)


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

    return graph(adjacency_list(adj_list))


def generate_probability(vertices_num, probability):
    if 0.0 > probability > 1.0:
        raise Exception("Probability domain [0, 1]")

    edge_list = list(combinations([i for i in range(vertices_num)], 2))

    adj_list = [[] for _ in range(vertices_num)]
    for i in range(len(edge_list)):
        if random.random() < probability:
            adj_list[edge_list[i][0]].append(edge_list[i][1])
            adj_list[edge_list[i][1]].append(edge_list[i][0])

    return graph(adjacency_list(adj_list))
