#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.base_model = BaseModel()

    def test_attributes(self):
        """Test the attributes of BaseModel."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_type(self):
        """Test the type of id attribute."""
        self.assertIsInstance(self.base_model.id, str)

    def test_timestamps(self):
        """Test the timestamps."""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        expected = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected)

    def test_save_method(self):
        """Test the save method."""
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_to_dict_method_keys(self):
        """Test if to_dict method returns all instance keys."""
        keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = self.base_model.to_dict()
        self.assertCountEqual(obj_dict.keys(), keys)


if __name__ == '__main__':
    unittest.main()

