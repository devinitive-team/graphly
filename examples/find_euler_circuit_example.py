from graphly.generator import generator
from graphly.algorithm import algorithm
from graphly.graph import graph

g = generator.generate("eulerian", 8)

# g = graph.from_file("eulerian_graph.json")

eulerian_circuit = algorithm.find_eulerian_circuit(g)
print(" -> ".join(map(str, eulerian_circuit)))

