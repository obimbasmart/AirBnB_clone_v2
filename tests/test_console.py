#!/usr/bin/python3

'''Unit Test for HBNB command Interpreter'''

from console import HBNBCommand
import unittest
from models import storage
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test for command interpreter"""

    def setUp(self):
        self.storage = storage
        self.storage.test_db_file = 'test_consele_db.json'

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
