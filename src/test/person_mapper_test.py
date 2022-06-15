import os
from unittest import TestCase, mock

from src.mapper.person_mapper import map_person_to_dict
from src.model.person import Person


@mock.patch.dict(os.environ, {"PROFILE": "Test"})
class PersonMapperTest(TestCase):

    def test_should_map_object_person_to_dict(self):
        #  GIVEN
        person = Person(1, 'Thiago')

        #  WHEN
        person_dict = map_person_to_dict(person)

        # THEN
        self.assertIsNotNone(person_dict)
        self.assertEqual(person_dict['id'], 1)
        self.assertEqual(person_dict['name'], 'Thiago')
