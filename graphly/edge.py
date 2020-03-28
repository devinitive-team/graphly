class edge:
    def __init__(self, edge_tuple, weight=1):
        self.edge_tuple = edge_tuple
        self.weight = weight

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "edge: ({e0}, {e1}), weight: {weight}".format(
            e0=self.edge_tuple[0],
            e1=self.edge_tuple[1],
            weight=self.weight)

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_tuple(self):
        return self.edge_tuple

    def set_tuple(self, edge_tuple):
        self.edge_tuple = edge_tuple
