class adjacency_list:
    def __init__(self, vertices):
        self.vertices = vertices
        self.vertices_num = len(vertices)

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def edges(self):
        return self.to_incidence_matrix().edges()

    def exchange_edges(self, edges):
        if edges[1][1] not in self.vertices[edges[0][0]] and edges[1][0] not in self.vertices[edges[0][1]]:
            self.vertices[edges[0][0]].append(edges[1][1])
            self.vertices[edges[1][1]].append(edges[0][0])
            self.vertices[edges[0][1]].append(edges[1][0])
            self.vertices[edges[1][0]].append(edges[0][1])
            self.vertices[edges[0][0]].remove(edges[0][1])
            self.vertices[edges[1][1]].remove(edges[1][0])
            self.vertices[edges[0][1]].remove(edges[0][0])
            self.vertices[edges[1][0]].remove(edges[1][1])
            for vert in self.vertices:
                vert.sort()

    def edge_exists(self, first_node, second_node):
        return self.to_adjacency_matrix().edge_exists(first_node, second_node)

    def nodes(self):
        return self.to_incidence_matrix().nodes()

    def to_adjacency_list(self):
        return self.vertices

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

    def exchange_edges(self, edges):
        print(self.vertices)
        print(edges)
        raise Exception

    def edge_exists(self, first_node, second_node):
        return True if self.vertices[first_node][second_node] != 0 else False

    def nodes(self):
        return self.to_incidence_matrix().nodes()

    def to_adjacency_matrix(self):
        return self.vertices

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

    def exchange_edges(self, edges):
        print(self.vertices)
        print(edges)
        raise Exception

    def edge_exists(self, first_node, second_node):
        return self.to_adjacency_matrix().edge_exists(first_node, second_node)

    def nodes(self):
        return [i for i in range(self.vertices_num)]

    def to_incidence_matrix(self):
        return self.vertices

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
