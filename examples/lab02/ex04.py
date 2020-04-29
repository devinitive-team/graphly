from graphly.generator import generator
from graphly.algorithm import algorithm

g = generator.generate("eulerian", 6)

g.plot("ex04.png")

algorithm.find_eulerian_circuit(g)


