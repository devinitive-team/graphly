from graphly.generator import generator
from graphly.plotter import plotter

flow_network = generator.generate("flow-network", 5)
plotter.plot_flow_digraph(flow_network, "ex01.png")
