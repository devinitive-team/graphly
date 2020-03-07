from core.graph.representation import *
from core.interfaces.printable import printable


class graph(printable):
    def __init__(self, graph_representation):
        self.graph_representation = graph_representation

    def print(self):
        self.graph_representation.print()

    def edges(self):
        return self.graph_representation.edges()

    def nodes(self):
        return self.graph_representation.nodes()
