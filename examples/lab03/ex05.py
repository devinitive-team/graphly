import random
from graphly.algorithm import algorithm
from graphly.generator import generator

g = generator.generate("random-connected", 10)
algorithm.randomize_graph(g, 3)
print(g.get_edges())

for e in g.get_edges():
    e.set_weight(random.randint(1, 10))

print(g.get_edges())
g.plot_weighted("ex05_1.png")

algorithm.prim_algorithm(g).plot_weighted("ex05_2.png")

