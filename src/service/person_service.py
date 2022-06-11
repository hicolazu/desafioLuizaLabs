import logging

from src.model.person import Person
from src.repository import person_repository
from src.builder.graph_builder import build_graph
from src.mapper.person_mapper import map_person_to_dict

logging.basicConfig(level=logging.INFO, force=True)


def get_all_person() -> [Person]:
    people = person_repository.find_all()

    return people


def get_friend_list(name: str) -> [Person]:
    person = person_repository.find_by_name(name)
    graph = build_graph()

    if person is not None:
        person = graph.get_node_by_id(person.id)

        people = person_repository.find_by_ids(person.friend_list)

        return people


def get_non_friend_list(name: str) -> [Person]:
    non_friend_id_list = []
    person = person_repository.find_by_name(name)

    friend_list = get_friend_list(person.name)
    friend_id_list = list(map(lambda x: x.id, friend_list))

    for friend in friend_list:
        friends_friend_list = get_friend_list(friend.name)

        for friend_of_friend in friends_friend_list:
            if (friend_of_friend.id not in friend_id_list) & (friend_of_friend.id is not person.id) & (friend_of_friend.id not in non_friend_id_list):
                non_friend_id_list.append(friend_of_friend.id)

    non_friend_list = person_repository.find_by_ids(non_friend_id_list)

    return non_friend_list


def save(name: str, friends_name_list: [str]) -> int:
    return person_repository.save(name, friends_name_list)
