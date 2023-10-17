#!/usr/bin/python3

"""
This module serves as a test script for the file storage engine of
using the unit test module
"""

from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Unit test for file storage class"""

    def setUp(self):
        """initialize fixtures for each test"""
        self.storage = storage
        self.storage.test_db_file = 'test_file.json'
        self.storage.reload()
        self.test_instance = BaseModel()
        self.test_instance.name = "Obimba Smart"
        self.test_instance.age = 100
        self.test_instance.save()

    def tearDown(self):
        """reset before each test"""
        if os.path.exists(self.storage.test_db_file):
            os.remove(self.storage.test_db_file)
        self.storage.all().clear()

    def test_all(self):
        """storage.all() should return all objects"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_file_path(self):
        """test correct file_path type"""
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_fileStorage_object(self):
        """storage object should have __object private property"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_init(self):
        """new objects should be saved to storage when instantianted"""
        new_obj = BaseModel()
        new_obj_dict = new_obj.to_dict()

        self.assertNotEqual(1,
                            len(self.storage.all()))
        self.assertEqual(2,
                         len(self.storage.all()))

        # object should not be saved when kwargs(dict) is passed constructor
        obj_dont_save = BaseModel(**new_obj_dict)
        self.assertEqual(2,
                         len(self.storage.all()))

    def test_new(self):
        """storage.new(obj) should add obj to @__storage"""
        new_obj = BaseModel()

        storage.new(new_obj)
        self.assertNotEqual(1,
                            len(storage.all()))
        self.assertEqual(2,
                         len(storage.all()))

    def test_save(self):
        """storage.save() should serialize object to json file"""
        self.test_instance.name = "New Name"
        id = self.test_instance.id
        self.storage.new(self.test_instance)
        self.storage.save()

        self.storage.all().clear()
        self.storage.reload()
        self.assertEqual(storage.all().get('BaseModel.' + id).name, "New Name")

    def test_reload(self):
        """storage.reload() should reload all object from file"""

        if os.path.exists(self.storage.test_db_file):
            os.remove(storage.test_db_file)

        storage.all().clear()
        storage.save()

        storage.reload()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all(), {})

        first_model = BaseModel()
        first_model.save()

        storage.reload()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(len(storage.all()), 1)
