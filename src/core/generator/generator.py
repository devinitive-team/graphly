import scipy.special
import random
from core.graph.graph import graph
from core.graph.representation import adjacency_list


def generate(vertices_num, edges_num):
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
