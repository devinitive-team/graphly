from graphly.algorithm import algorithm
from graphly.graph import graph

g = graph.from_file("data/hamiltonian.json")
print(algorithm.is_hamiltonian(g))
