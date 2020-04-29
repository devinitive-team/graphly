from graphly.generator import generator

seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

g = generator.generate("degree-seq", seq)
g.print()
g.plot("ex01.png")
