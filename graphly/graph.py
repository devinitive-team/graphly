from graphly.reader import reader
from graphly.plotter import plotter


class graph:
    def __init__(self, graph_representation):
        self.graph_representation = graph_representation
        self.edges = graph_representation.regenerate_edges()
        self.nodes = graph_representation.regenerate_nodes()

    @classmethod
    def from_file(cls, filepath):
        return cls(reader.read(filepath))

    def print(self):
        self.graph_representation.print()

    def exchange_edges(self, edges):
        self.graph_representation.to_adjacency_list().exchange_edges(edges)
        self.edges = self.graph_representation.regenerate_edges()

    def plot(self, name="graph.png"):
        plotter.plot(self, name)

    def plot_weighted(self, name="graph.png"):
        plotter.plot_weighted(self, name)

    def get_vertices(self):
        return self.graph_representation.vertices

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_edge(self, first_vertex, second_vertex):
        for e in self.edges:
            if first_vertex in e.edge_tuple and second_vertex in e.edge_tuple:
                return e

        raise Exception("Edge not found")

    def remove_edge(self, e):
        self.graph_representation.remove_edge_by_index(e)
        self.edges = self.graph_representation.regenerate_edges()

    def edge_exists(self, first_node, second_node):
        return self.graph_representation.edge_exists(first_node, second_node)

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
