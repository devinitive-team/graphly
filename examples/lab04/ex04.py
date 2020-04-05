from graphly.generator import generator
from graphly.algorithm import algorithm

di_g = generator.generate("strongly-connected-weighted-digraph", 3, 0.3, -3, 10)
di_g.plot_weighted()
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in algorithm.johnson_algorithm(di_g)]))
