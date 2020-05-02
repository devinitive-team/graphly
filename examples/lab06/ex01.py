from graphly.algorithm import algorithm
from graphly.digraph import digraph

dg = digraph.from_stochastic_matrix("data.json")
v = algorithm.pagerank_iterative(dg.get_as_numpy_array(), 1000, 0.15)
print(v)

dg = digraph.from_stochastic_matrix("data.json")
v = algorithm.pagerank_surfer(dg.get_as_numpy_array(), 1000, 0.15)
print(v)
