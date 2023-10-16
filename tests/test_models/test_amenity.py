#!/usr/bin/python3


"""Unit tests for Amenity class"""

from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Unit test for Amenity class"""

    __dummy_data = 'some test data'

    def setUp(self):
        """initialize fixtures for each test"""
        self.a1 = Amenity()

        self.a2_dict = {'id': '97b6c2ea860e47f39cc9fb1093abcf09',
                        'created_at': '2023-10-15T23:47:46.943126',
                        'updated_at': '2023-10-15T23:47:46.943126',
                        '__class__': 'Amenity'}

        self.a2_str = "[Amenity] (97b6c2ea860e47f39cc9fb1093abcf09) " \
            "{'id': '97b6c2ea860e47f39cc9fb1093abcf09', " \
            "'created_at': datetime.datetime(2023, 10, "\
            "15, 23, 47, 46, 943126), 'updated_at': datetime.datetime" \
            "(2023, 10, 15, 23, 47, 46, 943126)}"

        self.a2 = Amenity(**self.a2_dict)

    def test_init(self):
        """test instance initialization"""
        obj1 = Amenity()
        obj1_dict = obj1.to_dict()

        obj2 = Amenity(**obj1_dict)

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, Amenity)
        self.assertIsInstance(obj2, Amenity)

        self.assertEqual(self.a1.name, '')

        self.a1.name = "Television"

        self.assertEqual(self.a1.name, "Television")

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.a1.id, str)
        self.assertIsInstance(self.a2.id, str)

        self.assertIsInstance(self.a1.created_at, datetime)
        self.assertIsInstance(self.a2.created_at, datetime)

        self.assertIsInstance(self.a1.updated_at, datetime)
        self.assertIsInstance(self.a2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.a1, Amenity)
        self.assertIsInstance(self.a2, Amenity)

        self.assertIsInstance(self.a1, BaseModel)
        self.assertIsInstance(self.a2, BaseModel)

        self.assertNotEqual(self.a1, self.a2)
        self.assertNotEqual(self.a1.id, self.a2.id)
        self.assertNotEqual(self.a1.id, self.a2.id)

    def test_to_dict(self):
        """obj.to_dict() should return a dictionary of object attr:val"""
        self.assertEqual(self.a2.to_dict(), dict(self.a2_dict))
        self.assertIsInstance(self.a1.to_dict(), dict)
        self.assertIsInstance(self.a2.to_dict(), dict)

    def test_str(self):
        """test for correct string representation of object"""
        self.assertEqual(str(self.a2), self.a2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_a1 = self.a1.id
        initial_id_a2 = self.a2.id

        intital_update_time_a1 = self.a1.updated_at
        intital_update_time_a2 = self.a2.updated_at

        self.a1.name = "ObimbaSmart"
        self.a2.school = "Noun"

        self.a1.save()
        self.a2.save()

        self.assertEqual(self.a1.id, initial_id_a1)
        self.assertEqual(self.a2.id, initial_id_a2)

        self.assertNotEqual(self.a1.updated_at, initial_id_a1)
        self.assertNotEqual(self.a2.updated_at, intital_update_time_a2)

        self.assertEqual(self.a1.name, "ObimbaSmart")
        self.assertEqual(self.a2.school, "Noun")
