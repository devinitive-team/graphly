from graphly.generator import generator
from graphly.plotter import plotter

flow_network = generator.generate("flow-network", 2)
plotter.plot_digraph(flow_network, "ex01.png")
