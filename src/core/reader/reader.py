import json
from core.factory import graph as graph_factory


def read(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
        data_format = data["format"]
        vertices = []
        for vertex in data["data"]:
            vertices.append(vertex)

        return graph_factory.create(data_format, vertices)
