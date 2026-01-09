#!/usr/bin/python3
"""This module defines the FileStorage class for serialization."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes back."""
    __file_path = "file.json"
    __objects = {}

    # Map class names to classes for reload
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        if obj is None:
            raise AttributeError("obj cannot be None")
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects, if file exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                cls_name = val["__class__"]
                cls = FileStorage.classes.get(cls_name)
                if cls:
                    FileStorage.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass
