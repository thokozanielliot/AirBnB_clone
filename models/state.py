#!/usr/bin/python3
"""Define a State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a State

    Attributes:
        name(string)
    """
    name = ""

    def __int__(self, *args, **kwargs):
        """Initializes State"""
        super().__init__(*args, **kwargs)
