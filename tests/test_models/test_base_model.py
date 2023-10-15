#!/usr/bin/python3


"""Unit tests for BaseModel class"""

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
        self.assertIsInstance(self.m1, BaseModel)
        self.assertIsInstance(self.m2, BaseModel)
        self.assertNotEqual(self.m1, self.m2)
        self.assertNotEqual(self.m1.id, self.m2.id)
        self.assertNotEqual(self.m1.id, self.m3.id)

    def test_to_dict(self):
        self.assertEqual(self.m2.to_dict(), dict(self.m2_dict))

    def test_str(self):
        self.assertEqual(str(self.m2), self.m2_str)

    def test_save(self):
        initial_id_m1 = self.m1.id
        initial_id_m2 = self.m2.id

        self.m1.name = "ObimbaSmart"
        self.m2.School = "Noun"

        self.m1.save()
        self.m2.save()

        self.assertEqual(self.m1.id, initial_id_m1)
        self.assertEqual(self.m2.id, initial_id_m2)
