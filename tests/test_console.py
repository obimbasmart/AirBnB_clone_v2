#!/usr/bin/python3

'''Unit Test for HBNB command Interpreter'''

from console import HBNBCommand
import unittest
from models import storage
from unittest.mock import patch
from io import StringIO
import os


class TestConsole(unittest.TestCase):
    """Test for command interpreter"""

    def setUp(self):
        self.storage = storage
        self.storage.test_db_file = 'test_consele_db.json'
        self.storage.all().clear()
        self.storage.save()

    def tearDown(self):
        self.storage.all().clear()
        self.storage.save()

    def test_quit(self):
        ''' test `quit` command'''
        with patch('sys.stdout', new=StringIO()) as f:
            ret = HBNBCommand().onecmd("quit")
            self.assertEqual(ret, True)
            f.close()

    def test_EOF(self):
        ''' test `EOF` command'''
        with patch('sys.stdout', new=StringIO()) as f:
            ret = HBNBCommand().onecmd("EOF")
            self.assertEqual(ret, True)
            f.close()

    def test_empty_line(self):
        ''' test `emptyline`'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue())
            f.close()

    def test_BaseModel(self):
        ''' test `BaseModel.all()` command'''

        # all
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.all()')
            self.assertEqual("[]\n", f.getvalue())
            f.close()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            self.assertEqual("[]\n", f.getvalue())
            f.close()

        # count
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.count()')
            self.assertEqual("0\n", f.getvalue())
            f.close()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.count()')
            self.assertEqual("0\n", f.getvalue())
            f.close()

    def test_User(self):
        ''' test `User.all()` command'''

        # all
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.all()')
            self.assertEqual("[]\n", f.getvalue())
            f.close()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            self.assertEqual("[]\n", f.getvalue())
            f.close()

        # count
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
            self.assertEqual("0\n", f.getvalue())
            f.close()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
            self.assertEqual("0\n", f.getvalue())
            f.close()
