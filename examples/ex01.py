import random
from graphly.generator import generator

g = generator.generate("random-connected", 10)

print(g.get_edges())

for e in g.get_edges():
    e.set_weight(random.randint(1, 10))

print(g.get_edges())
g.plot_weighted("ex01.png")
