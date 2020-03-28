from operator import itemgetter
from graphly.algorithm import algorithm
from graphly.reader import reader
from graphly.plotter import plotter
from graphly.representation import representation


class graph:
    def __init__(self, graph_representation):
        self.graph_representation = graph_representation
        self.edges = graph_representation.regenerate_edges()
        self.nodes = graph_representation.regenerate_nodes()

    @classmethod
    def from_file(cls, filepath):
        return cls(reader.read(filepath))

    @classmethod
    def from_degree_seq(cls, sequence):
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

        return cls(representation.adjacency_list(adj_list))

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

    def remove_edge(self, e):
        self.graph_representation.remove_edge(e)
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
