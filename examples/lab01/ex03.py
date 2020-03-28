from graphly.generator import generator

g = generator.generate("normal", 7, 14)
g.plot()

g = generator.generate("probability", 15, 0.05)
g.plot()
