from uuid import uuid4
from datetime import datetime

class BaseModel():
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        from models import storage

        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.strptime(
                            v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """return string representation"""
        clnmae = self.__class__.__name__
        return "[{}] ({}) {}".format(clnmae, self.id, self.__dict__)

    def save(self):
        from models import storage

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Return a dict representation of an instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
