from core.generator import generator
from core.plotter import plotter
from core.reader import reader


def main():
    print("Graphly!")
    generator.generate()
    plotter.plot()
    reader.read("/path/filepath")


if __name__ == "__main__":
    main()
