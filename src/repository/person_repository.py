from src.model.person import Person


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
