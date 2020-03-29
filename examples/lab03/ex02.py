import random
from graphly.algorithm import algorithm
from graphly.generator import generator

g = generator.generate("random-connected", 5)
algorithm.randomize_graph(g, 3)

for e in g.get_edges():
    e.set_weight(random.randint(1, 10))

g.plot_weighted("ex02.png")


shortest_paths = algorithm.dijkstra_algorithm(g)

i = 0
for sp in shortest_paths:
    print(f"d({i}) = {sp}")
    i += 1
