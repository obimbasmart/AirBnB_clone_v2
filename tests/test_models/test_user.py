#!/usr/bin/python3


"""Unit tests for User class"""

from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Unit test for User class"""

    __dummy_data = 'some test data'

    def setUp(self):
        """initialize fixtures for each test"""
        self.u1 = User()

        self.u2_dict = {'id': '97b6c2ea860e47f39cc9fb1093abcf09',
                        'created_at': '2023-10-15T23:47:46.943126',
                        'updated_at': '2023-10-15T23:47:46.943126',
                        '__class__': 'User'}

        self.u2_str = "[User] (97b6c2ea860e47f39cc9fb1093abcf09) " \
            "{'id': '97b6c2ea860e47f39cc9fb1093abcf09', " \
            "'created_at': datetime.datetime(2023, 10, "\
            "15, 23, 47, 46, 943126), 'updated_at': datetime.datetime" \
            "(2023, 10, 15, 23, 47, 46, 943126)}"

        self.u2 = User(**self.u2_dict)

    def test_init(self):
        """test instance initialization"""
        obj1 = User()
        obj1_dict = obj1.to_dict()

        obj2 = User(**obj1_dict)

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, User)
        self.assertIsInstance(obj2, User)

        self.assertEqual(self.u1.last_name, '')
        self.assertEqual(self.u1.first_name, '')
        self.assertEqual(self.u1.password, '')
        self.assertEqual(self.u1.email, '')

        self.u1.last_name = "Smart"
        self.u1.first_name = "Obimba"
        self.u1.password = "12345"
        self.u1.email = "obimbasmart@gmail.com"

        self.assertEqual(self.u1.last_name, "Smart")
        self.assertEqual(self.u1.first_name, "Obimba")
        self.assertEqual(self.u1.password, "12345")
        self.assertEqual(self.u1.email, "obimbasmart@gmail.com")

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.u1.id, str)
        self.assertIsInstance(self.u2.id, str)

        self.assertIsInstance(self.u1.created_at, datetime)
        self.assertIsInstance(self.u2.created_at, datetime)

        self.assertIsInstance(self.u1.updated_at, datetime)
        self.assertIsInstance(self.u2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.u1, User)
        self.assertIsInstance(self.u2, User)

        self.assertIsInstance(self.u1, BaseModel)
        self.assertIsInstance(self.u2, BaseModel)

        self.assertNotEqual(self.u1, self.u2)
        self.assertNotEqual(self.u1.id, self.u2.id)
        self.assertNotEqual(self.u1.id, self.u2.id)

    def test_to_dict(self):
        """obj.to_dict() should return a dictionary of object attr:val"""
        self.assertEqual(self.u2.to_dict(), dict(self.u2_dict))
        self.assertIsInstance(self.u1.to_dict(), dict)
        self.assertIsInstance(self.u2.to_dict(), dict)

    def test_str(self):
        """test for correct string representation of object"""
        self.assertEqual(str(self.u2), self.u2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_u1 = self.u1.id
        initial_id_u2 = self.u2.id

        intital_update_time_u1 = self.u1.updated_at
        intital_update_time_u2 = self.u2.updated_at

        self.u1.name = "ObimbaSmart"
        self.u2.school = "Noun"

        self.u1.save()
        self.u2.save()

        self.assertEqual(self.u1.id, initial_id_u1)
        self.assertEqual(self.u2.id, initial_id_u2)

        self.assertNotEqual(self.u1.updated_at, initial_id_u1)
        self.assertNotEqual(self.u2.updated_at, intital_update_time_u2)

        self.assertEqual(self.u1.name, "ObimbaSmart")
        self.assertEqual(self.u2.school, "Noun")
