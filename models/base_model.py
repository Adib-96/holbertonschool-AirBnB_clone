#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for models that represent objects"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the __dict__ representation of an instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
