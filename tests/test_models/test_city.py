#!/usr/bin/python3


"""Unit tests for City class"""

from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Unit test for City class"""

    def setUp(self):
        """initialize fixtures for each test"""
        self.c1 = City()

        self.c2_dict = {'id': '97b6c2ea860e47f39cc9fb1093abcf09',
                        'created_at': '2023-10-15T23:47:46.943126',
                        'updated_at': '2023-10-15T23:47:46.943126',
                        '__class__': 'City'}

        self.c2_str = "[City] (97b6c2ea860e47f39cc9fb1093abcf09) " \
            "{'id': '97b6c2ea860e47f39cc9fb1093abcf09', " \
            "'created_at': datetime.datetime(2023, 10, "\
            "15, 23, 47, 46, 943126), 'updated_at': datetime.datetime" \
            "(2023, 10, 15, 23, 47, 46, 943126)}"

        self.c2 = City(**self.c2_dict)

    def test_init(self):
        """test instance initialization"""
        obj1 = City()
        obj1_dict = obj1.to_dict()

        obj2 = City(**obj1_dict)

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, City)
        self.assertIsInstance(obj2, City)

        self.assertEqual(self.c1.name, '')

        self.c1.name = "AriaraMarket"
        self.assertEqual(self.c1.name, "AriaraMarket")

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.c1.id, str)
        self.assertIsInstance(self.c2.id, str)

        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c2.created_at, datetime)

        self.assertIsInstance(self.c1.updated_at, datetime)
        self.assertIsInstance(self.c2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.c1, City)
        self.assertIsInstance(self.c2, City)

        self.assertIsInstance(self.c1, BaseModel)
        self.assertIsInstance(self.c2, BaseModel)

        self.assertNotEqual(self.c1, self.c2)
        self.assertNotEqual(self.c1.id, self.c2.id)
        self.assertNotEqual(self.c1.id, self.c2.id)

    def test_to_dict(self):
        """obj.to_dict() should return a dictionary of object attr:val"""
        self.assertEqual(self.c2.to_dict(), dict(self.c2_dict))
        self.assertIsInstance(self.c1.to_dict(), dict)
        self.assertIsInstance(self.c2.to_dict(), dict)

    def test_str(self):
        """test for correct string representation of object"""
        self.assertEqual(str(self.c2), self.c2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_c1 = self.c1.id
        initial_id_c2 = self.c2.id

        intital_update_time_c1 = self.c1.updated_at
        intital_update_time_c2 = self.c2.updated_at

        self.c1.name = "ObimbaSmart"
        self.c2.school = "Noun"

        self.c1.save()
        self.c2.save()

        self.assertEqual(self.c1.id, initial_id_c1)
        self.assertEqual(self.c2.id, initial_id_c2)

        self.assertNotEqual(self.c1.updated_at, initial_id_c1)
        self.assertNotEqual(self.c2.updated_at, intital_update_time_c2)

        self.assertEqual(self.c1.name, "ObimbaSmart")
        self.assertEqual(self.c2.school, "Noun")
