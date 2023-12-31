#!/usr/bin/python3
"""Define a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a City class

    Attributes:
        state_id(string)
        name(string)
    """
    state_id = ""
    name = ""

    def __int__(self, *args, **kwargs):
        """Initializes City"""
        super().__init__(*args, **kwargs)
