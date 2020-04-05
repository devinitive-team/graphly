from graphly.edge import edge


class adjacency_list:
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.vertices_num = len(vertices)
        self.is_directed = is_directed
        self.edges = self.to_incidence_matrix().regenerate_edges()

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def regenerate_nodes(self):
        return self.to_incidence_matrix().regenerate_nodes()

    def regenerate_edges(self):
        return self.to_incidence_matrix().regenerate_edges()

    def remove_edge(self, e):
        return self.to_incidence_matrix().remove_edge(e)

    def copy(self):
        return adjacency_list(self.vertices[:], self.is_directed)

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

    def to_adjacency_list(self):
        return self

    def to_adjacency_matrix(self):
        if self.is_directed:
            raise Exception("Not implemented for directed graphs.")
        else:
            matrix = [self.vertices_num * [0] for _ in range(self.vertices_num)]

            for i in range(self.vertices_num):
                for j in self.vertices[i]:
                    matrix[i][j] = 1

            return adjacency_matrix(matrix)

    def to_incidence_matrix(self):
        if self.is_directed:
            num_edges = sum(len(vertex) for vertex in self.vertices)
            matrix = [num_edges * [0] for _ in range(self.vertices_num)]

            edge_index = 0
            for i in range(self.vertices_num):
                for j in self.vertices[i]:
                    matrix[i][edge_index] = -1
                    matrix[j][edge_index] = 1
                    edge_index += 1

            return incidence_matrix(matrix, self.is_directed)
        else:
            num_edges = sum(len(vertex) for vertex in self.vertices) // 2
            matrix = [num_edges * [0] for _ in range(self.vertices_num)]

            edge_index_map = {}
            for i in range(self.vertices_num):
                for j in self.vertices[i]:
                    e = tuple(sorted([i, j]))
                    if e not in edge_index_map:
                        edge_index_map[e] = len(edge_index_map)
                    edge_index = edge_index_map[e]
                    matrix[i][edge_index] = 1

            return incidence_matrix(matrix, self.is_directed)


class adjacency_matrix:
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.is_directed = is_directed
        self.edges = self.to_incidence_matrix().regenerate_edges()

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def regenerate_nodes(self):
        return self.to_incidence_matrix().regenerate_nodes()

    def regenerate_edges(self):
        return self.to_incidence_matrix().regenerate_edges()

    def remove_edge(self, e):
        return self.to_incidence_matrix().remove_edge(e)

    def exchange_edges(self, edges):
        print(self.vertices)
        print(edges)
        raise Exception

    def edge_exists(self, first_node, second_node):
        return True if self.vertices[first_node][second_node] != 0 else False

    def to_adjacency_matrix(self):
        return self.vertices

    def to_adjacency_list(self):
        if self.is_directed:
            raise Exception("Not implemented for directed graphs.")
        else:
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
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.edges_num = len(self.vertices[0])
        self.is_directed = is_directed
        self.vertices_num = len(self.vertices)

    def print(self):
        for i in range(len(self.vertices)):
            print(f"{i}: {self.vertices[i]}")

    def regenerate_nodes(self):
        return [i for i in range(self.vertices_num)]

    def regenerate_edges(self):
        if self.is_directed:
            edges_list = []

            for j in range(self.edges_num):
                current_edge = [0, 0]
                weight = 1
                for i in range(self.vertices_num):
                    if self.vertices[i][j] < 0:
                        current_edge[0] = i
                    elif self.vertices[i][j] > 0:
                        current_edge[1] = i
                        weight = self.vertices[i][j]
                edges_list.append(edge(current_edge, weight))

            return edges_list
        else:
            edges_list = []
            for j in range(self.edges_num):
                current_edge = []
                weight = 1
                for i in range(self.vertices_num):
                    if self.vertices[i][j] != 0:
                        current_edge.append(i)
                        weight = self.vertices[i][j]
                edges_list.append(edge(current_edge, weight))

            return edges_list

    def remove_edge(self, e):
        if self.is_directed:
            raise Exception("Not implemented for directed graphs.")
        else:
            if e >= self.edges_num:
                raise Exception("Edge does not exist")

            for i in range(self.vertices_num):
                self.vertices[i][e] = 0

    def exchange_edges(self, edges):
        print(self.vertices)
        print(edges)
        raise Exception("Not implemented.")

    def edge_exists(self, first_node, second_node):
        return self.to_adjacency_matrix().edge_exists(first_node, second_node)

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
