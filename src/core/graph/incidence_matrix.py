from core.interfaces.printable import printable


class incidence_matrix(printable):
    def __init__(self, vertices):
        self.vertices = vertices

    def print(self):
        print(self.vertices)
