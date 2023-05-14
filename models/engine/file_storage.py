#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name == 'BaseModel':
                        cls = BaseModel
                    elif class_name == 'State':
                        cls = State
                    elif class_name == 'City':
                        cls = City
                    elif class_name == 'Amenity':
                        cls = Amenity
                    elif class_name == 'Place':
                        cls = Place
                    elif class_name == 'Review':
                        cls = Review
                    else:
                        continue
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        classes = {"BaseModel": BaseModel, "User": User}  # Add User class mapping
