from graphly.algorithm import algorithm
from graphly.generator import generator
from graphly.plotter import plotter

g = algorithm.ford_fulkerson(generator.generate("flow-network", 4), 0, 1)
plotter.plot_flow_digraph(g, 'ex02g.png')

for e in g.get_edges():
    print(f"edge: {e.get_tuple()}")
    print(f"flow: {e.get_flow()} ")
    print(f"capacity: {e.get_capacity()}\n")

