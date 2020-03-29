import random
from graphly.algorithm import algorithm
from graphly.generator import generator

g = generator.generate("random-connected", 10)
algorithm.randomize_graph(g, 3)

for e in g.get_edges():
    e.set_weight(random.randint(1, 10))

print(f"Matrix center (index): {algorithm.calculate_center(g)}")
print(f"Matrix minmax center (index): {algorithm.calculate_minmax_center(g)}")
