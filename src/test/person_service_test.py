import os
from unittest import TestCase, mock

import src.service.person_service as service
from src.model.person import Person


@mock.patch.dict(os.environ, {"PROFILE": "Test"})
class PersonServiceTest(TestCase):

    def should_return_all_people(self):
        # GIVEN
        # file with people persisted

        # WHEN
        people: [Person] = service.get_all_person()

        # THEN
        self.assertIsNotNone(people)
        self.assertTrue(len(people) >= 6)

    def should_return_all_friends(self):
        # GIVEN
        person_name = 'Ana'

        # WHEN
        friends: [Person] = service.get_friend_list(person_name)

        # THEN
        self.assertIsNotNone(friends)
        self.assertEqual(4, len(friends))

    def should_return_all_non_friends(self):
        # GIVEN
        person_name = 'Ana'

        # WHEN
        friends: [Person] = service.get_non_friend_list(person_name)

        # THEN
        self.assertIsNotNone(friends)
        self.assertEqual(1, len(friends))
        self.assertEqual('Luiza', friends[0].name)

    def should_save_new_person(self):
        # GIVEN
        person_name = 'Thiago'
        friends_name_list = ['Ana']

        # WHEN
        id = service.save(person_name, friends_name_list)

        # THEN
        self.assertIsNotNone(id)

    def should_raise_exception_when_save_if_friend_doesnt_exist(self):
        # GIVEN
        person_name = 'Matheus'
        friends_name_list = ['Jandir']

        # THEN
        with self.assertRaises(Exception):
            # WHEN
            id = service.save(person_name, friends_name_list)
