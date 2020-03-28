from graphly.generator import generator
from graphly.algorithm import algorithm

g = generator.generate("eulerian", 8)

eulerian_circuit = algorithm.find_eulerian_circuit(g)
print(" -> ".join(map(str, eulerian_circuit)))
