#!/usr/bin/python3
"""
Modules that serializes instances to a JSON file
and deserializes JSON file to instance
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes(class_attributes):
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        obj_key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_key, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for key, obj_data in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = globals()[cls_name]
                    obj = cls(**obj_data)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
