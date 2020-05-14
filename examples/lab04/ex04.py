from graphly.generator import generator
from graphly.algorithm import algorithm

di_g = generator.generate("strongly-connected-weighted-digraph", 8, 0.3, -2, 10)
di_g.plot_weighted("ex04_weighted.png")

for el in di_g.edges:
    print(el)

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in algorithm.johnson_algorithm(di_g)]))


