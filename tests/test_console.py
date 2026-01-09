#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand console"""

    def setUp(self):
        """Clear storage before each test"""
        storage._FileStorage__objects = {}

    def test_create_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_and_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(len(obj_id) > 0)

        # Test show
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)
            self.assertIn("BaseModel", output)

    def test_destroy(self):
        # Create first
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        # Destroy it
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(), "")

        # Try to show again
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        HBNBCommand().onecmd("create BaseModel")
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_update(self):
        # create object
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        # update attribute
        HBNBCommand().onecmd(f'update BaseModel {obj_id} name "TestName"')

        # show to check
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn("'name': 'TestName'", output)

    def test_update_errors(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        # create obj
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel 1234 name Test")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj_id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")


if __name__ == "__main__":
    unittest.main()
