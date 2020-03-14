from graphly.algorithm import algorithm
from graphly.graph import graph

seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

if algorithm.degree_seq(seq):
    g = graph.from_degree_seq(seq)
    g.plot()
