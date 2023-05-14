#!/usr/bin/python3
"""Defines unittests for console.py.


Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import sys
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import os
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        self.cli = HBNBCommand()
    
    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test_prompt(self):
        self.assertEqual("(hbnb) ", self.cli.prompt)
    
    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("\n")
            self.assertEqual("", f.getvalue().strip())
    
    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("quit")
            self.assertEqual("", f.getvalue().strip())
    
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())
    
    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)
    
    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("[BaseModel]", f.getvalue())
    
    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("destroy BaseModel {}".format(obj_id))
            self.cli.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("** no instance found **", f.getvalue())
    
    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("create User")
            self.cli.onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("[BaseModel]", output)
            self.assertIn("[User]", output)
    
    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.cli.onecmd("update BaseModel {} name 'new name'".format(obj_id))
            self.cli.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn("'name': 'new name'", f.getvalue())
    
    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("create User")
            self.cli.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual("2", output)
    
    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("invalid")
            self.assertEqual("** Unknown command **", f.getvalue().strip())

if __name__ == '__main__':
    unittest.main()

