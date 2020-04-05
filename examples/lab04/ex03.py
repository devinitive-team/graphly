from graphly.generator import generator
from graphly.algorithm import algorithm

di_g = generator.generate("strongly-connected-weighted-digraph", 6, 0.3, -5, 10)

di_g.plot_weighted("ex03_weighted.png")

print(algorithm.bellman_ford_algorithm(di_g)[0])
