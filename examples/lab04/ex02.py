from graphly.generator import generator
from graphly.algorithm import algorithm

di_g = generator.generate("probability-digraph", 6, 0.3)
di_g.plot("ex01.png")
di_g.plot_weighted("ex01_weighted.png")

di_g.plot_components(algorithm.kosaraju_algorithm(di_g), "ex02_components.png")


