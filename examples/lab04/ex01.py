from graphly.generator import generator

di_g = generator.generate("probability-digraph", 6, 0.3)
di_g.plot("ex01.png")
di_g.plot_weighted("ex01_weighted.png")
