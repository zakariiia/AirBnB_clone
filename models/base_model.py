#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Represent BaseModel of the HBnB project."""

    def __init__(self, *arg, **kwarg):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwarg:
            for key, value in kwarg.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(value, tform))
                else:
                    setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        """Update updated_at with the current date time."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Return the dic to basemodel."""
        instan_dict = self.__dict__.copy()
        instan_dict["__class__"] = self.__class__.__name__
        instan_dict["created_at"] = self.created_at.isoformat()
        instan_dict["updated_at"] = self.updated_at.isoformat()

        return instan_dict

    def __str__(self):
        """Return or print the instance of the base model."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
