from graphly.reader import reader
from graphly.plotter import plotter
from graphly.representation import representation
import json

import numpy as np


class digraph:
    def __init__(self, graph_representation = None, from_stochastic_matrix=False, data = None):
        if not from_stochastic_matrix:
            self.graph_representation = graph_representation
            self.edges = graph_representation.regenerate_edges()
            self.nodes = graph_representation.regenerate_nodes()
        else:
            self.data = data

    def transpose_edges(self):
        return [(e.edge_tuple[1], e.edge_tuple[0]) for e in self.edges]

    @classmethod
    def from_file(cls, filepath):
        return cls(reader.read(filepath))

    @classmethod
    def from_stochastic_matrix(cls, filepath):
        with open(filepath) as json_file:
            data = json.load(json_file)
            data_format = data["format"]
            vertices = []
            for vertex in data["data"]:
                vertices.append(vertex)

        return cls(data=np.array(vertices), from_stochastic_matrix=True)

    def get_as_numpy_array(self):
        return self.data

    @classmethod
    def from_nodes_edges(cls, nodes, edges):
        adj_list = [[] for _ in range(len(nodes))]

        for e in edges:
            u, v = e.get_tuple()
            adj_list[u].append(v)

        return cls(representation.adjacency_list(adj_list, True))

    def print(self):
        self.graph_representation.print()

    def exchange_edges(self, edges):
        self.graph_representation.to_adjacency_list().exchange_edges(edges)
        self.edges = self.graph_representation.regenerate_edges()

    def plot(self, name="digraph.png"):
        plotter.plot_digraph(self, name)

    def plot_weighted(self, name="digraph.png"):
        plotter.plot_weighted_digraph(self, name)

    def plot_components(self, components, name="digraph.png"):
        plotter.plot_with_component(self, components, name)

    def get_vertices(self):
        return self.graph_representation.vertices

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_edge(self, first_vertex, second_vertex):
        for e in self.edges:
            u, v = e.edge_tuple
            if u == first_vertex and v == second_vertex:
                return e

        raise Exception("Edge not found")

    def remove_edge_by_index(self, e_index):
        self.graph_representation.remove_edge_by_index(e_index)
        self.edges = self.graph_representation.regenerate_edges()

    def remove_edge(self, e):
        self.edges.remove(e)

    def add_edge(self, e):
        self.edges.append(e)

    def edge_exists(self, first_node, second_node):
        return self.graph_representation.edge_exists(first_node, second_node)

    def copy(self):
        return digraph(self.graph_representation.copy())

    def get_adjacency_list(self):
        return self.graph_representation.to_adjacency_list()

    def get_adjacency_matrix(self):
        return self.graph_representation.to_adjacency_matrix()

    def get_incidence_matrix(self):
        return self.graph_representation.to_incidence_matrix()

    def set_representation(self, representation_string):
        self.graph_representation = {
            "adjacency_list": self.get_adjacency_list,
            "adjacency_matrix": self.get_adjacency_matrix,
            "incidence_matrix": self.get_incidence_matrix
        }[representation_string]()
