#!/usr/bin/python3


"""Unit tests for Place class"""

from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Unit test for Place class"""

    __dummy_data = 'some test data'

    def setUp(self):
        """initialize fixtures for each test"""
        self.p1 = Place()

        self.p2_dict = {'id': '97b6c2ea860e47f39cc9fb1093abcf09',
                        'created_at': '2023-10-15T23:47:46.943126',
                        'updated_at': '2023-10-15T23:47:46.943126',
                        '__class__': 'Place'}

        self.p2_str = "[Place] (97b6c2ea860e47f39cc9fb1093abcf09) " \
            "{'id': '97b6c2ea860e47f39cc9fb1093abcf09', " \
            "'created_at': datetime.datetime(2023, 10, "\
            "15, 23, 47, 46, 943126), 'updated_at': datetime.datetime" \
            "(2023, 10, 15, 23, 47, 46, 943126)}"

        self.p2 = Place(**self.p2_dict)

    def test_init(self):
        """test instance initialization"""
        obj1 = Place()
        obj1_dict = obj1.to_dict()

        obj2 = Place(**obj1_dict)

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, Place)
        self.assertIsInstance(obj2, Place)

        self.assertEqual(self.p1.city_id, '')
        self.assertEqual(self.p1.user_id, '')
        self.assertEqual(self.p1.name, '')
        self.assertEqual(self.p1.amenity_id, [])
        self.assertEqual(self.p1.description, '')
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertEqual(self.p1.max_guest, 0)
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertEqual(self.p1.latitude, 0.0)

        self.p1.max_guest = 4
        self.assertEqual(self.p1.max_guest, 4)

        self.p1.last_name = "Smart"
        self.p1.first_name = "Obimba"
        self.p1.password = "12345"
        self.p1.email = "obimbasmart@gmail.com"

        self.assertEqual(self.p1.last_name, "Smart")
        self.assertEqual(self.p1.first_name, "Obimba")
        self.assertEqual(self.p1.password, "12345")
        self.assertEqual(self.p1.email, "obimbasmart@gmail.com")

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.p1.id, str)
        self.assertIsInstance(self.p2.id, str)

        self.assertIsInstance(self.p1.created_at, datetime)
        self.assertIsInstance(self.p2.created_at, datetime)

        self.assertIsInstance(self.p1.updated_at, datetime)
        self.assertIsInstance(self.p2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.p1, Place)
        self.assertIsInstance(self.p2, Place)

        self.assertIsInstance(self.p1, BaseModel)
        self.assertIsInstance(self.p2, BaseModel)

        self.assertNotEqual(self.p1, self.p2)
        self.assertNotEqual(self.p1.id, self.p2.id)
        self.assertNotEqual(self.p1.id, self.p2.id)

    def test_to_dict(self):
        """obj.to_dict() should return a dictionary of object attr:val"""
        self.assertEqual(self.p2.to_dict(), dict(self.p2_dict))
        self.assertIsInstance(self.p1.to_dict(), dict)
        self.assertIsInstance(self.p2.to_dict(), dict)

    def test_str(self):
        """test for correct string representation of object"""
        self.assertEqual(str(self.p2), self.p2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_p1 = self.p1.id
        initial_id_p2 = self.p2.id

        intital_update_time_p1 = self.p1.updated_at
        intital_update_time_p2 = self.p2.updated_at

        self.p1.name = "ObimbaSmart"
        self.p2.school = "Noun"

        self.p1.save()
        self.p2.save()

        self.assertEqual(self.p1.id, initial_id_p1)
        self.assertEqual(self.p2.id, initial_id_p2)

        self.assertNotEqual(self.p1.updated_at, initial_id_p1)
        self.assertNotEqual(self.p2.updated_at, intital_update_time_p2)

        self.assertEqual(self.p1.name, "ObimbaSmart")
        self.assertEqual(self.p2.school, "Noun")
