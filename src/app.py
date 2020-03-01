from core.generator import generator
from core.plotter import plotter
from core.reader import reader


def main():
    print("Graphly!")
    graph = reader.read("../examples/adjacency_list_graph.json")
    graph.print()


if __name__ == "__main__":
    main()
