class node:
    def __init__(self, index, visited=False):
        self.index = index
        self.visited = visited

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "index: {index}, visited: {visited}".format(
            index=self.index,
            visited=self.visited)

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited
