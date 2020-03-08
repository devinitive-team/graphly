import json
from graphly.factory import factory


def read(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
        data_format = data["format"]
        vertices = []
        for vertex in data["data"]:
            vertices.append(vertex)

        return factory.create_graph(data_format, vertices)
