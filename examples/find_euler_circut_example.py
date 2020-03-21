from graphly.generator import generator
from graphly.algorithm import algorithm


g = generator.generate("eulerian", 8)
print(algorithm.is_eulerian(g))
g.plot("eulerian.png")
