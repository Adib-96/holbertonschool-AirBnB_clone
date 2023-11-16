#!/usr/bin/python3
"""
Modules that define a class for storing objects
"""
from models.base_model import BaseModel
import json
import datetime


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
        """serializes __objects to the JSON file
        (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            dict = {}
            for k, v in self.__objects.items():
                dict[k] = v.to_dict()
            json.dump(dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist
        no exception should be raised)"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.load(f)
                for k, v in dict.items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except FileNotFoundError:
            pass
