class adjacency_list:
    def __init__(self, vertices):
        self.vertices = vertices
        self.vertices_num = len(vertices)

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def edges(self):
        return self.to_incidence_matrix().edges()

    def nodes(self):
        return self.to_incidence_matrix().nodes()

    def to_adjacency_matrix(self):
        matrix = [self.vertices_num * [0] for _ in range(self.vertices_num)]

        for i in range(self.vertices_num):
            for j in self.vertices[i]:
                matrix[i][j] = 1

        return adjacency_matrix(matrix)

    def to_incidence_matrix(self):
        num_edges = sum(len(vertex) for vertex in self.vertices) // 2
        matrix = [num_edges * [0] for _ in range(self.vertices_num)]

        edge_index_map = {}
        for i in range(self.vertices_num):
            for j in self.vertices[i]:
                edge = tuple(sorted([i, j]))
                if edge not in edge_index_map:
                    edge_index_map[edge] = len(edge_index_map)
                edge_index = edge_index_map[edge]
                matrix[i][edge_index] = 1

        return incidence_matrix(matrix)


class adjacency_matrix:
    def __init__(self, vertices):
        self.vertices = vertices

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def edges(self):
        return self.to_incidence_matrix().edges()

    def nodes(self):
        return self.to_incidence_matrix().nodes()

    def to_adjacency_list(self):
        adj_list = []
        for i in range(len(self.vertices)):
            adj_list.append([])
            for j in range(len(self.vertices[i])):
                if self.vertices[i][j] != 0:
                    adj_list[i].append(j)

        return adjacency_list(adj_list)

    def to_incidence_matrix(self):
        return self.to_adjacency_list().to_incidence_matrix()


class incidence_matrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges_num = len(self.vertices[0])
        self.vertices_num = len(self.vertices)

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def edges(self):
        edges_list = []
        for j in range(self.edges_num):
            current_edge = []
            for i in range(self.vertices_num):
                if self.vertices[i][j] == 1:
                    current_edge.append(i)
            edges_list.append(current_edge)

        return edges_list

    def nodes(self):
        return [i for i in range(self.vertices_num)]

    def to_adjacency_list(self):
        adj_list = []
        for i in range(self.vertices_num):
            adj_list.append([])
            for j in range(self.edges_num):
                if self.vertices[i][j] == 1:
                    for k in range(self.vertices_num):
                        if k == i:
                            continue
                        elif self.vertices[k][j] == 1:
                            adj_list[i].append(k)

        return adjacency_list(adj_list)

    def to_adjacency_matrix(self):
        return self.to_adjacency_list().to_adjacency_matrix()
