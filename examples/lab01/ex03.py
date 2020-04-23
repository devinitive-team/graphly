from graphly.generator import generator

g = generator.generate("normal", 12, 12)
g.plot("ex03_1.png")

g = generator.generate("probability", 7, 1)
g.plot("ex03_2.png")
