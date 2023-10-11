#!/usr/bin/python3
"""Define the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """A class representing the BaseMode of AirBnB project"""

    def __init__(self, *args, **kwargs):
        """
        Initialize instances
        """
        #self.id = str(uuid4())
        #self.created_at = datetime.today()
        #self.update_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "update_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.today()
            if "update_at" not in kwargs:
                self.update_at = datetime.today()
        else:
            self.id = str(uuid4())
            self.created_at = self.update_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Update update_at with current datetime"""
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a ditionary conatining all key/values of  __dict__ of the instance"""
        create_at = self.created_at.isoformat()
        update_at = self.update_at.isoformat()
        #self.created_at = create_at.isoformat()
        #self.update_at = update_at.isoformat()
        
        dictCopy = self.__dict__.copy()
        dictCopy["created_at"] = create_at
        dictCopy["update_at"] = update_at
        dictCopy["__class__"] = self.__class__.__name__
        
        return dictCopy
        """return {
            "__class__": self.__class__.__name__,
            "update_at": self.update_at,
            "id": self.id,
            "created_at": self.created_at
        }"""

    
    def __str__(self):
        """Special representation for printing a string"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
