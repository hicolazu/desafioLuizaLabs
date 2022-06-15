import os
from unittest import TestCase, mock

import src.repository.person_repository as repository
from src.model.person import Person


@mock.patch.dict(os.environ, {"PROFILE": "Test"})
class PersonRepositoryTest(TestCase):

    def should_return_all_people(self):
        # GIVEN
        # file with people persisted

        # WHEN
        people: [Person] = repository.find_all()

        # THEN
        self.assertIsNotNone(people)
        self.assertTrue(len(people) >= 6)

    def should_return_person_by_name(self):
        # GIVEN
        person_name = 'Ana'

        # WHEN
        person: Person = repository.find_by_name(person_name)

        # THEN
        self.assertIsNotNone(person)
        self.assertEqual('Ana', person.name)

    def should_return_people_by_ids(self):
        # GIVEN
        people_ids = [1, 2]

        # WHEN
        people: [Person] = repository.find_by_ids(people_ids)

        # THEN
        self.assertIsNotNone(people)
        self.assertEqual(2, len(people))

    def should_return_people_by_names(self):
        # GIVEN
        people_names = ['Ana', 'Luiza']

        # WHEN
        people: [Person] = repository.find_by_names(people_names)

        # THEN
        self.assertIsNotNone(people)
        self.assertEqual(2, len(people))

    def should_return_last_id(self):
        # GIVEN
        # persisted list of id's

        # WHEN
        last_id: int = repository.get_last_id()

        # THEN
        self.assertIsNotNone(last_id)
        self.assertTrue(last_id >= 6)

    def should_save_new_person(self):
        # GIVEN
        person_name = 'José'
        friends_name_list = ['Ana']

        # WHEN
        id = repository.save(person_name, friends_name_list)

        # THEN
        self.assertIsNotNone(id)

    def should_raise_exception_when_save_if_friend_doesnt_exist(self):
        # GIVEN
        person_name = 'Matheus'
        friends_name_list = ['Jandir']

        # THEN
        with self.assertRaises(Exception):
            # WHEN
            id = repository.save(person_name, friends_name_list)
