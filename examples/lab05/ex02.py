from graphly.algorithm import algorithm
from graphly.generator import generator
from graphly.plotter import plotter

g = generator.generate("flow-network", 3)
plotter.plot_flow_digraph(g, "ex02.png")
algorithm.ford_fulkerson(g, 0, 1)
