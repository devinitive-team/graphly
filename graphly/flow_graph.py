from graphly.digraph import digraph


class flow_graph(digraph):
    def __init__(self, graph_representation):
        super().__init__(graph_representation)
        self.layers = []

    def set_layers(self, layers):
        self.layers = layers

    def get_layers(self):
        return self.layers
