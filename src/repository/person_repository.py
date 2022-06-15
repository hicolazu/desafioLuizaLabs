from model.person import Person


def find_all() -> [Person]:
    people = []

    with open("people.txt", "r") as file:
        for line in file.readlines():
            line = line.split()
            if len(line) > 1:
                person = Person(int(line[0]), line[1])
                people.append(person)

    return people


def find_by_name(name: str) -> Person:
    with open("people.txt", "r") as file:
        for line in file.readlines():
            line = line.split()
            if len(line) > 1:
                if line[1] == name:
                    return Person(int(line[0]), line[1])

    return None


def find_by_ids(ids: [int]) -> [Person]:
    people = []

    with open("people.txt", "r") as file:
        for line in file.readlines():
            line = line.split()
            if len(line) > 1:
                if ids.__contains__(int(line[0])):
                    person = Person(int(line[0]), line[1])
                    people.append(person)

    return people


def find_by_names(names: [str]) -> [Person]:
    people = []

    with open("people.txt", "r") as file:
        for line in file.readlines():
            line = line.split()
            if len(line) > 1:
                if names.__contains__(line[1]):
                    person = Person(int(line[0]), line[1])
                    people.append(person)

    return people


def get_last_id() -> int:
    last_id = 0

    with open("people.txt", "r") as file:
        for line in file.readlines():
            line = line.split()
            if len(line) > 1:
                last_id = int(line[0])

    return last_id


def save(name: str, friends_name_list: [str]) -> int:
    last_id = get_last_id()

    new_person = Person(last_id+1, name)

    friend_list = find_by_names(friends_name_list)

    if len(friend_list) != len(friends_name_list):
        raise Exception('One or more friends not found!')

    with open("people.txt", "a") as file:
        file.write(str(new_person.id) + ' ' + new_person.name + '\n')

    with open("friends.pajek", "a") as file:
        for friend in friend_list:
            file.write(str(new_person.id) + ' ' + str(friend.id) + '\n')

    return new_person.id
