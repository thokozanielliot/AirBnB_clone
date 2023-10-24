#!/usr/bin/python3
"""Define the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A class representing the BaseMode of AirBnB project"""

    def __init__(self, *args, **kwargs):
        """
        Initialize instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if hasattr(self, "created_at") and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs["created_at"], time_format)
                if hasattr(self, "updated_at") and type(self.updated_at) is str:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], time_format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a ditionary conatining all key/values of
        __dict__ of the instance
        """
        dictCopy = self.__dict__.copy()
        if "created_at" in dictCopy:
            dictCopy["created_at"] = dictCopy["created_at"].strftime(time_format)
        if "updated_at" in dictCopy:
            dictCopy["updated_at"] = dictCopy["updated_at"].strftime(time_format)
        dictCopy["__class__"] = self.__class__.__name__
        return dictCopy

    def __str__(self):
        """Special representation for printing a string"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
