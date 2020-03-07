from core.generator import generator
from core.plotter import plotter
from core.reader import reader
from core.graph.graph import graph


def main():
    print("Graphly!")

    # my_graph = generator.generate("normal", 1000, 100000)
    # plotter.plot(my_graph)

    my_graph = generator.generate("probability", 25, 0.1)
    plotter.plot(my_graph)


if __name__ == "__main__":
    main()
