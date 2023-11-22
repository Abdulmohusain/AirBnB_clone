#!/usr/bin/python3
""" Test for FileStorage class """
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestDefault(unittest.TestCase):
    """ This is a test for FileStorage class """

    def test_empty_line(self):
        """Test Empty line"""
        HBNBCommand().onecmd("")

    def test_quit(self):
        """Test quit command"""
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF"""
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_unknown_command(self):
        """Test unknown command"""
        expected_out = "*** Unknown syntax: wsjsj\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("wsjsj")
        self.assertEqual(expected_out, output.getvalue())


class TestHelp(unittest.TestCase):
    """ This is a test for FileStorage class """

    def test_help_unknown_command(self):
        """Test unknown command"""
        expected_out = "*** No help on wsjsj\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help wsjsj")
        self.assertEqual(expected_out, output.getvalue())

    def test_help_create(self):
        """Test help command"""
        expected_out = "Create instance of a class and saves it as json\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
        self.assertEqual(expected_out, output.getvalue())

    def test_help_delete(self):
        """Test help destroy"""
        expected_out = "Delete an instance of a class\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
        self.assertEqual(expected_out, output.getvalue())


class TestCreate(unittest.TestCase):
    """ This is a test for FileStorage class """
    def test_create_no_class(self):
        """Test create command"""
        expected_out = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
        self.assertEqual(expected_out, output.getvalue())

    def test_create_wrong_class(self):
        """Test create command"""
        expected_out = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create asdfg")
        self.assertEqual(expected_out, output.getvalue())

    def test_create_with_class(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
        self.assertTrue(output.getvalue())


class TestShow(unittest.TestCase):
    """ This is a test for FileStorage class """

    def test_show_no_class(self):
        """Test show without class"""
        expected_out = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
        self.assertEqual(expected_out, output.getvalue())

    def test_show_wrong_class(self):
        """Test show without class"""
        expected_out = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show asdf")
        self.assertEqual(expected_out, output.getvalue())

    def test_show_class_no_id(self):
        """Test show without class"""
        expected_out = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show User")
        self.assertEqual(expected_out, output.getvalue())

    def test_show_class_wrong_id(self):
        """Test show without class"""
        expected_out = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show User ssjj")
        self.assertEqual(expected_out, output.getvalue())

    def test_show_correct_case(self):
        """Test show without class"""
        model = BaseModel()

        expected_out = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show User {}".format(model.id))
        self.assertEqual(expected_out, output.getvalue())


class TestDestroy(unittest.TestCase):
    """test destroy feature in console"""
    def test_no_class(self):
        """test if no class is entered"""
        correct = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(correct, output.getvalue())

    def test_wrong_class(self):
        """test with wrong class"""
        correct = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy Myclass")
        self.assertEqual(correct, output.getvalue())

    def test_class_no_id(self):
        """test class with no id"""
        correct = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(correct, output.getvalue())

    def test_correct_output(self):
        """test correct command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        test_id = output.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as output:
            instance = models.storage.all()["BaseModel.{}".format(test_id)]
            HBNBCommand().onecmd("destroy BaseModel.{}".format(test_id))
            self.assertNotIn(instance, models.storage.all())


if __name__ == "__main__":
    unittest.main()
