from core.graph.adjacency_list import adjacency_list
from core.graph.adjacency_matrix import adjacency_matrix
from core.graph.incidence_matrix import incidence_matrix


def create(data_format, vertices):
    return {
        "adjacency_matrix": adjacency_matrix,
        "adjacency_list": adjacency_list,
        "incidence_matrix": incidence_matrix,
    }[data_format]()
