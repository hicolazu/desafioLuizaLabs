import logging

from src.repository import person_repository
from src.builder.graph_builder import build_graph
from src.mapper.person_mapper import map_person_to_dict

logging.basicConfig(level=logging.INFO, force=True)


def get_all_person() -> [dict]:
    people = person_repository.find_all()

    people_dict = list(map(lambda x: map_person_to_dict(x), people))

    return people_dict


def get_friend_list(name: str) -> [dict]:
    person = person_repository.find_by_name(name)
    graph = build_graph()

    if person is not None:
        person = graph.get_node_by_id(person.id)

        people = person_repository.find_by_ids(person.friend_list)

        people_dict = list(map(lambda x: map_person_to_dict(x), people))

        return people_dict

