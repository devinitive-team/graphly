class edge:
    def __init__(self, edge_tuple, weight=1, visited=False):
        self.edge_tuple = edge_tuple
        self.weight = weight
        self.visited = visited

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"edge: ({self.edge_tuple[0]}, {self.edge_tuple[1]}), weight: {self.weight}, visited: {self.visited}"

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_tuple(self):
        return self.edge_tuple

    def set_tuple(self, edge_tuple):
        self.edge_tuple = edge_tuple

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited
