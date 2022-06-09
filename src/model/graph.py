from src.model.person import Person


class Graph:
    def __init__(self):
        self.nodes = []
        self.n = 0

    def add_node(self, node: Person) -> None:
        self.nodes.append(node)
        self.n += 1

    def add_edge(self, first_person_id: int, second_person_id: int) -> None:
        first_person: Person = list(filter(lambda x: x.id == first_person_id, self.nodes))[0]
        second_person: Person = list(filter(lambda x: x.id == second_person_id, self.nodes))[0]

        first_person.add_friend(second_person_id)
        second_person.add_friend(first_person_id)

    def get_node_by_id(self, id: int) -> Person:
        for node in self.nodes:
            if node.id == id:
                return node
