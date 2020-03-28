from pprint import pformat, pprint
from graphly.algorithm import algorithm
from graphly.graph import graph

g = graph.from_file("data/disconnected_graph.json")
components, largest_component = algorithm.largest_component(g)

formatted = pformat(components, indent=2)
pprint(formatted)
print(f"Largest component: {largest_component}")
