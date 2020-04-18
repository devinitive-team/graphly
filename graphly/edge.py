class edge:
    def __init__(self, edge_tuple, weight=1, capacity=10, visited=False):
        self.edge_tuple = edge_tuple
        self.weight = weight
        self.capacity = capacity
        self.visited = visited

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"edge: ({self.edge_tuple[0]}, {self.edge_tuple[1]}), weight: {self.weight}, visited: {self.visited}"

    def __eq__(self, other):
        return self.edge_tuple == other.edge_tuple and self.weight == other.weight and self.capacity == other.capacity and self.visited == other.visited

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_tuple(self):
        return self.edge_tuple

    def set_tuple(self, edge_tuple):
        self.edge_tuple = edge_tuple

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited
