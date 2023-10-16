#!/usr/bin/python3
"""Define a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a User
    
    Attributes:
        email(string)
        password(string)
        first_name(string)
        last_name(string)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    