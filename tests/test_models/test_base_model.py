#!/usr/bin/python3


"""Unit tests for BaseModel class"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    '''Unit tests for BaseModel class'''

    def setUp(self):
        self.m1 = BaseModel()
        self.m2 = BaseModel()

    def tearDown(self) -> None:
        pass

    def test_init(self):
        self.assertIsInstance(self.m1, BaseModel)
