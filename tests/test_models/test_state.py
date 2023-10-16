#!/usr/bin/python3


"""Unit tests for State class"""

from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Unit test for State class"""

    def setUp(self):
        """initialize fixtures for each test"""
        self.s1 = State()

        self.s2_dict = {'id': '97b6c2ea860e47f39cc9fb1093abcf09',
                        'created_at': '2023-10-15T23:47:46.943126',
                        'updated_at': '2023-10-15T23:47:46.943126',
                        '__class__': 'State'}

        self.s2_str = "[State] (97b6c2ea860e47f39cc9fb1093abcf09) " \
            "{'id': '97b6c2ea860e47f39cc9fb1093abcf09', " \
            "'created_at': datetime.datetime(2023, 10, "\
            "15, 23, 47, 46, 943126), 'updated_at': datetime.datetime" \
            "(2023, 10, 15, 23, 47, 46, 943126)}"
        self.s2 = State(**self.s2_dict)

    def test_init(self):
        """test instance initialization"""
        obj1 = State()
        obj1_dict = obj1.to_dict()

        obj2 = State(**obj1_dict)

        self.assertEqual(self.s1.state_id, '')
        self.assertEqual(self.s1.name, '')

        self.s1.name = "Abia"
        self.assertEqual(self.s1.name, "Abia")

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, State)
        self.assertIsInstance(obj2, State)

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.s1.id, str)
        self.assertIsInstance(self.s2.id, str)

        self.assertIsInstance(self.s1.created_at, datetime)
        self.assertIsInstance(self.s2.created_at, datetime)

        self.assertIsInstance(self.s1.updated_at, datetime)
        self.assertIsInstance(self.s2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.s1, State)
        self.assertIsInstance(self.s2, State)

        self.assertIsInstance(self.s1, BaseModel)
        self.assertIsInstance(self.s2, BaseModel)

        self.assertNotEqual(self.s1, self.s2)
        self.assertNotEqual(self.s1.id, self.s2.id)
        self.assertNotEqual(self.s1.id, self.s2.id)

    def test_to_dict(self):
        """obj.to_dict() should return a dictionary of object attr:val"""
        self.assertEqual(self.s2.to_dict(), dict(self.s2_dict))
        self.assertIsInstance(self.s1.to_dict(), dict)
        self.assertIsInstance(self.s2.to_dict(), dict)

    def test_str(self):
        """test for correct string representation of object"""
        self.assertEqual(str(self.s2), self.s2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_s1 = self.s1.id
        initial_id_s2 = self.s2.id

        intital_update_time_s1 = self.s1.updated_at
        intital_update_time_s2 = self.s2.updated_at

        self.s1.name = "ObimbaSmart"
        self.s2.school = "Noun"

        self.s1.save()
        self.s2.save()

        self.assertEqual(self.s1.id, initial_id_s1)
        self.assertEqual(self.s2.id, initial_id_s2)

        self.assertNotEqual(self.s1.updated_at, initial_id_s1)
        self.assertNotEqual(self.s2.updated_at, intital_update_time_s2)

        self.assertEqual(self.s1.name, "ObimbaSmart")
        self.assertEqual(self.s2.school, "Noun")
