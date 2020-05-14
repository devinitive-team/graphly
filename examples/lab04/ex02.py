from graphly.generator import generator
from graphly.algorithm import algorithm

di_g = generator.generate("probability-digraph", 6, 0.3)
di_g.plot("ex02.png")
di_g.plot_weighted("ex02_weighted.png")
for el in di_g.edges:
    print(el)
print(algorithm.kosaraju_algorithm(di_g))
di_g.plot_components(algorithm.kosaraju_algorithm(di_g), "ex02_components.png")


