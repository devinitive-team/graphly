from graphly.generator import generator
from graphly.algorithm import algorithm
from graphly.graph import graph

# g = graph.from_file("eulerian_graph.json")

g = generator.generate("eulerian")
# print(algorithm.is_eulerian(g))
g = generator.generate_eulerian(8)
g.plot()
