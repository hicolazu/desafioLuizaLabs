from model.graph import Graph
from repository import person_repository


def build_graph() -> Graph:
    graph = Graph()
    people = person_repository.find_all()

    for person in people:
        graph.add_node(person)

    with open("friends.pajek", "r") as file:
        for line in file.readlines():
            line = line.split()
            if len(line) > 1:
                graph.add_edge(int(line[0]), int(line[1]))

    return graph
