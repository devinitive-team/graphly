from graphly.reader import reader
from graphly.plotter import plotter
from graphly.representation import representation


class graph:
    def __init__(self, graph_representation):
        self.graph_representation = graph_representation

    @classmethod
    def from_file(cls, filepath):
        return cls(reader.read(filepath))

    @classmethod
    def from_degree_seq(cls, sequence):
        adj_list = [[] for _ in range(len(sequence))]
        sequence.sort(reverse=True)
        for i in range(len(sequence)):
            counter = 0
            j = i + 1
            while counter < sequence[i]:
                if sequence[j] > 0:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
                    sequence[j] -= 1
                    counter += 1
                j += 1

        return cls(representation.adjacency_list(adj_list))

    def print(self):
        self.graph_representation.print()

    def exchange_edges(self, edges):
        self.graph_representation.exchange_edges(edges)

    def plot(self, name="graph.png"):
        plotter.plot(self, name)

    def edges(self):
        return self.graph_representation.edges()

    def nodes(self):
        return self.graph_representation.nodes()
