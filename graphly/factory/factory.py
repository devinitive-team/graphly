from graphly.representation.representation import *


def create_graph(data_format, vertices):
    return {
        "adjacency_matrix": adjacency_matrix,
        "adjacency_list": adjacency_list,
        "incidence_matrix": incidence_matrix,
    }[data_format](vertices)
