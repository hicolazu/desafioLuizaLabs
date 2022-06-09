from src.model.person import Person


def map_person_to_dict(person: Person) -> dict:
    person_dict = person.__dict__
    del person_dict['friend_list']
    return person_dict
