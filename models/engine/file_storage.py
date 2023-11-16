#!/usr/bin/python3
from models.base_model import BaseModel
import json
import datetime
"""
Modules that define a class for storing objects
"""


class FileStorage():
    """A class for serializes/deserializes instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add a new instance ID to the dictionary(__objects)."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.item():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj = class_obj(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
