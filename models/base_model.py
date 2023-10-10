#!/usr/bin/python3
"""Define the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A class representing the BaseMode of AirBnB project"""

    def __init__(self, id = None):
        """
        Initialize instances
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.update_at = datetime.today()

    def save(self):
        """Update update_at with current datetime"""
        self.update_at = datetime.today()

    def to_dict(self):
        """Return a ditionary conatining all key/values of  __dict__ of the instance"""
        create_at = self.created_at
        update_at = self.update_at
        self.created_at = create_at.isoformat()
        self.update_at = update_at.isoformat()
        
        dictCopy = self.__dict__.copy()
        dictCopy["created_at"] = self.created_at
        dictCopy["update_at"] = self.update_at
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
