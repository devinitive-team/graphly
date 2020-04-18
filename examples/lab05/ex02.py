import random
from graphly.algorithm import algorithm
from graphly.generator import generator
from graphly.plotter import plotter

g = generator.generate("flow-network", 2)

# for e in g.get_edges():
#     e.set_flow(random.randint(0, e.get_capacity()))

gg = algorithm.ford_fulkerson(g, 0, 1)
plotter.plot_flow_digraph(gg, 'ex02g.png')

for e in gg.get_edges():
    print(f"edge: {e.get_tuple()}")
    print(f"flow: {e.get_flow()} ")
    print(f"capacity: {e.get_capacity()}\n")

