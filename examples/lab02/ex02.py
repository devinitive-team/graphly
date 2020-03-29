from graphly.algorithm import algorithm
from graphly.generator import generator

seq = [2, 2, 2, 2, 2, 2, 2]

if algorithm.is_degree_seq(seq):
    g = generator.generate("degree-seq", seq)
    g.plot("g1.png")
    algorithm.randomize_graph(g, 3)
    g.plot("g2.png")
