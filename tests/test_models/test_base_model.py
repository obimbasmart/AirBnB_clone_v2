#!/usr/bin/python3


"""Unit tests for BaseModel class"""

from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    '''Unit tests for BaseModel class'''

    def setUp(self):
        self.m1 = BaseModel()
        self.m2_dict = {'id': '5c45b3711ac7483e958eab56c6f50d25',
                        'created_at': '2023-10-15T20:51:26.856283',
                        'updated_at': '2023-10-15T20:51:26.856358',
                        '__class__': 'BaseModel'}

        self.m2 = BaseModel(**self.m2_dict)

        self.m2_str = "[BaseModel] (5c45b3711ac7483e958eab56c6f50d25) " \
            "{'id': '5c45b3711ac7483e958eab56c6f50d25', 'created_at': "\
            "datetime.datetime(2023, 10, 15, 20, 51, 26, 856283), " \
            "'updated_at': datetime.datetime" \
            "(2023, 10, 15, 20, 51, 26, 856358)}"

        self.m3 = BaseModel()

    def tearDown(self) -> None:
        pass

    def test_init(self):
        """test instance initialization"""
        obj1 = BaseModel()
        obj1_dict = obj1.to_dict()

        obj2 = BaseModel(obj1_dict)

        self.assertNotEqual(obj1, obj2)
        self.assertIsInstance(obj1, BaseModel)
        self.assertIsInstance(obj2, BaseModel)

    def test_types(self):
        """test for instance attribute and types"""
        self.assertIsInstance(self.m1.id, str)
        self.assertIsInstance(self.m2.id, str)

        self.assertIsInstance(self.m1.created_at, datetime)
        self.assertIsInstance(self.m2.created_at, datetime)

        self.assertIsInstance(self.m1.updated_at, datetime)
        self.assertIsInstance(self.m2.updated_at, datetime)

    def test_init_2(self):
        """test for correct instance creation and proper ID"""
        self.assertIsInstance(self.m1, BaseModel)
        self.assertIsInstance(self.m2, BaseModel)
        self.assertNotEqual(self.m1, self.m2)
        self.assertNotEqual(self.m1.id, self.m2.id)
        self.assertNotEqual(self.m1.id, self.m3.id)

    def test_to_dict(self):
        self.assertEqual(self.m2.to_dict(), dict(self.m2_dict))
        self.assertIsInstance(self.m1.to_dict(), dict)
        self.assertIsInstance(self.m2.to_dict(), dict)

    def test_str(self):
        self.assertEqual(str(self.m2), self.m2_str)

    def test_save(self):
        """test the save() method of BaseModel"""
        initial_id_m1 = self.m1.id
        initial_id_m2 = self.m2.id

        intital_update_time_m1 = self.m1.updated_at
        intital_update_time_m2 = self.m2.updated_at

        self.m1.name = "ObimbaSmart"
        self.m2.school = "Noun"

        self.m1.save()
        self.m2.save()

        self.assertEqual(self.m1.id, initial_id_m1)
        self.assertEqual(self.m2.id, initial_id_m2)

        self.assertNotEqual(self.m1.updated_at, initial_id_m1)
        self.assertNotEqual(self.m2.updated_at, intital_update_time_m2)

        self.assertEqual(self.m1.name, "ObimbaSmart")
        self.assertEqual(self.m2.school, "Noun")
