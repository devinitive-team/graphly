import random
from graphly.algorithm import algorithm
from graphly.generator import generator

g = generator.generate("random-connected", 10)
algorithm.randomize_graph(g, 3)

for e in g.get_edges():
    e.set_weight(random.randint(1, 10))

matrix = []

for v in range(len(g.get_vertices())):
    matrix.append(algorithm.dijkstra_algorithm(g, v))

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
