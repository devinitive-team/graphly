from graphly.reader import reader
from graphly.plotter import plotter


class graph:
    def __init__(self, graph_representation):
        self.graph_representation = graph_representation

    @classmethod
    def from_file(cls, filepath):
        return cls(reader.read(filepath))

    def print(self):
        self.graph_representation.print()

    def plot(self):
        plotter.plot(self)

    def edges(self):
        return self.graph_representation.edges()

    def nodes(self):
        return self.graph_representation.nodes()
