# Class Implementation of Person Node
class Person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.friend_list = []  # list of adjacent nodes

    def add_friend(self, friend_id: int) -> None:
        self.friend_list.append(friend_id)
