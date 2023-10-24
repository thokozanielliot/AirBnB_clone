#!/usr/bin/python3
"""Define an Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent an Amenity class

    Attributes:
        name(String)
    """
    name = ""

    def __int__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
