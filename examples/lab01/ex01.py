from graphly.graph import graph

print("From adjacency_matrix_graph.json")
g = graph.from_file("data/adjacency_matrix_graph.json")

g.print()
print()
g.graph_representation.to_adjacency_list().print()
print()
g.graph_representation.to_incidence_matrix().print()

print("From adjacency_list_graph.json")

g = graph.from_file("data/adjacency_list_graph.json")

g.print()
print()
g.graph_representation.to_adjacency_matrix().print()
print()
g.graph_representation.to_incidence_matrix().print()

print("From incidence_matrix_graph.json")

g = graph.from_file("data/incidence_matrix_graph.json")

g.print()
print()
g.graph_representation.to_adjacency_matrix().print()
print()
g.graph_representation.to_adjacency_list().print()
