from graphly.algorithm import algorithm
from graphly.graph import graph

g = graph.from_file("disconnected_graph.json")
algorithm.largest_component(g)
