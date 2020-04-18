class edge:
    def __init__(self, edge_tuple, weight=1, capacity=10, flow=0, residual_capacity=0, visited=False):
        self.edge_tuple = edge_tuple
        self.weight = weight
        self.flow = flow
        self.capacity = capacity
        self.visited = visited
        self.residual_capacity = residual_capacity

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

    def set_flow(self, flow):
        self.flow = flow

    def get_flow(self):
        return self.flow

    def set_residual_capacity(self, residual_capacity):
        self.residual_capacity = residual_capacity

    def get_residual_capacity(self):
        return self.residual_capacity
