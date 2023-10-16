#!/usr/bin/python3


"""Unit tests for BaseModel class"""

from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Unit test for Review class"""

    def setUp(self):
        """initialize fixtures for each test"""
        self.r1 = Review()

        self.r2_dict = {'id': '97b6c2ea860e47f39cc9fb1093abcf09',
                        'created_at': '2023-10-15T23:47:46.943126',
                        'updated_at': '2023-10-15T23:47:46.943126',
                        '__class__': 'Review'}

        self.r2_str = "[Review] (97b6c2ea860e47f39cc9fb1093abcf09) " \
            "{'id': '97b6c2ea860e47f39cc9fb1093abcf09', " \
            "'created_at': datetime.datetime(2023, 10, "\
            "15, 23, 47, 46, 943126), 'updated_at': datetime.datetime" \
            "(2023, 10, 15, 23, 47, 46, 943126)}"

        self.r2 = Review(**self.r2_dict)

    def test_init(self):
        """test instance initialization"""
        obj1 = Review()
        obj1_dict = obj1.to_dict()

        obj2 = Review(**obj1_dict)

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, Review)
        self.assertIsInstance(obj2, Review)

        self.assertEqual(self.r1.place_id, '')
        self.assertEqual(self.r1.user_id, '')
        self.assertEqual(self.r1.text, '')

        self.r1.place_id = "1234567"
        self.r1.user_id = "999999"
        self.r1.text = "This house is good"

        self.assertEqual(self.r1.place_id, "1234567")
        self.assertEqual(self.r1.user_id, "999999")
        self.assertEqual(self.r1.text, "This house is good")

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.r1.id, str)
        self.assertIsInstance(self.r2.id, str)

        self.assertIsInstance(self.r1.created_at, datetime)
        self.assertIsInstance(self.r2.created_at, datetime)

        self.assertIsInstance(self.r1.updated_at, datetime)
        self.assertIsInstance(self.r2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.r1, Review)
        self.assertIsInstance(self.r2, Review)

        self.assertIsInstance(self.r1, BaseModel)
        self.assertIsInstance(self.r2, BaseModel)

        self.assertNotEqual(self.r1, self.r2)
        self.assertNotEqual(self.r1.id, self.r2.id)
        self.assertNotEqual(self.r1.id, self.r2.id)

    def test_to_dict(self):
        """obj.to_dict() should return a dictionary of object attr:val"""
        self.assertEqual(self.r2.to_dict(), dict(self.r2_dict))
        self.assertIsInstance(self.r1.to_dict(), dict)
        self.assertIsInstance(self.r2.to_dict(), dict)

    def test_str(self):
        """test for correct string representation of object"""
        self.assertEqual(str(self.r2), self.r2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_r1 = self.r1.id
        initial_id_r2 = self.r2.id

        intital_update_time_r1 = self.r1.updated_at
        intital_update_time_r2 = self.r2.updated_at

        self.r1.name = "ObimbaSmart"
        self.r2.school = "Noun"

        self.r1.save()
        self.r2.save()

        self.assertEqual(self.r1.id, initial_id_r1)
        self.assertEqual(self.r2.id, initial_id_r2)

        self.assertNotEqual(self.r1.updated_at, initial_id_r1)
        self.assertNotEqual(self.r2.updated_at, intital_update_time_r2)

        self.assertEqual(self.r1.name, "ObimbaSmart")
        self.assertEqual(self.r2.school, "Noun")
