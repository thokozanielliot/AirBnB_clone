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