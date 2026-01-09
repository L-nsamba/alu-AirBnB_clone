#!/usr/bin/python3
"""
FileStorage class
Serializes instances to a JSON file and deserializes back to instances
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)

            cls_dict = {
                "BaseModel": BaseModel,
                "User": User
            }

            for key, value in data.items():
                cls_name = value["__class__"]
                self.__objects[key] = cls_dict[cls_name](**value)

        except FileNotFoundError:
            pass
