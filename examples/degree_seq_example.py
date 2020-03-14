from graphly.algorithm import algorithm
from graphly.graph import graph

seq = [2, 2, 2, 2, 2, 2]

if algorithm.is_degree_seq(seq):
    g = graph.from_degree_seq(seq)
    g.plot("g1.png")
    algorithm.randomize_graph(g, 2)
    g.plot("g2.png")

