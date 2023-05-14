#!/usr/bin/python3
"""Unit tests for FileStorage class."""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test cases."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test case."""
        self.storage.reset()

    def test_all(self):
        """Test the all method of FileStorage."""
        # Create a new BaseModel instance
        model = BaseModel()
        model.save()

        # Retrieve all objects from storage
        all_objs = self.storage.all()

        # Check if the object is in the returned dictionary
        self.assertIn(model.__class__.__name__ + "." + model.id, all_objs)

    def test_new(self):
        """Test the new method of FileStorage."""
        # Create a new BaseModel instance
        model = BaseModel()

        # Add the object to storage
        self.storage.new(model)

        # Check if the object is in the dictionary of objects
        self.assertIn(model.__class__.__name__ + "." + model.id, self.storage._FileStorage__objects)

    def test_save(self):
        """Test the save method of FileStorage."""
        # Create a new BaseModel instance
        model = BaseModel()
        model.save()

        # Save the objects to the JSON file
        self.storage.save()

        # Read the contents of the JSON file
        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_content = file.read()

        # Check if the object's data is present in the JSON file
        self.assertIn(model.__class__.__name__ + "." + model.id, file_content)

    def test_reload(self):
        """Test the reload method of FileStorage."""
        # Create a new BaseModel instance
        model = BaseModel()
        model.save()

        # Save the objects to the JSON file
        self.storage.save()

        # Clear the objects in memory
        self.storage.reset()

        # Reload the objects from the JSON file
        self.storage.reload()

        # Check if the object is in the dictionary of objects
        self.assertIn(model.__class__.__name__ + "." + model.id, self.storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
