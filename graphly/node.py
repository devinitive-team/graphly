class node:
    def __init__(self, index: object = None, visited: object = False):
        self.index = index
        self.visited = visited

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"(index: {self.index}, visited: {self.visited})"

    def __eq__(self, other):
        return self.index == other.index and self.visited == other.visited

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited
