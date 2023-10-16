#!/usr/bin/python3

"""
This module serves as a test script for the file storage engine of
using the unit test module
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Unit test for file storage class"""

    __storage = {}
    __file_path = 'file.json'

    @classmethod
    def setUpClass(cls):
        TestFileStorage.__storage = FileStorage()
        TestFileStorage.__storage.reload()

    def setUp(self):
        self.initial_object_count = len(TestFileStorage.__storage.all())

    def tearDown(self):
        pass

    def test_all(self):
        """storage.all() should return all objects"""
        self.assertIsInstance(TestFileStorage.__storage.all(), dict)

    def test_init(self):
        """new objects should be saved to storage when instantianted"""
        new_obj = BaseModel()
        new_obj_dict = new_obj.to_dict()

        self.assertNotEqual(self.initial_object_count,
                            len(TestFileStorage.__storage.all()))
        self.assertEqual(self.initial_object_count + 1,
                         len(TestFileStorage.__storage.all()))

        # object should not be saved when kwargs(dict) is passed constructor
        obj_dont_save = BaseModel(**new_obj_dict)
        self.assertEqual(self.initial_object_count + 1,
                         len(TestFileStorage.__storage.all()))

    def test_new(self):
        """storage.new(obj) should add obj to @__storage"""
        new_obj = BaseModel()

        TestFileStorage.__storage.new(new_obj)
        self.assertNotEqual(self.initial_object_count,
                            len(TestFileStorage.__storage.all()))
        self.assertEqual(self.initial_object_count + 1,
                         len(TestFileStorage.__storage.all()))

    def test_reload(self):
        """storage.reload() should reload all object from file"""
        TestFileStorage.__storage.reload()
        self.assertIsInstance(TestFileStorage.__storage.all(), dict)
