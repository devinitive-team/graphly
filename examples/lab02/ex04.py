from graphly.generator import generator
from graphly.algorithm import algorithm

g = generator.generate("eulerian", 5)

g.plot()

algorithm.find_eulerian_circuit(g)


