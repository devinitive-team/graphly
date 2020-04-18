import random
from graphly.algorithm import algorithm
from graphly.generator import generator
from graphly.plotter import plotter

g = generator.generate("flow-network", 2)

# for e in g.get_edges():
#     e.set_flow(random.randint(0, e.get_capacity()))

gg, c_f = algorithm.ford_fulkerson(g, 0, 1)
print(c_f)

plotter.plot_flow_digraph(g, 'ex02g.png')
plotter.plot_flow_digraph(gg, 'ex02.png')
