#!/usr/bin/python3
"""Define a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent a Review

    Attributes:
        place_id(string)
        user_id(string)
        text(string)
    """
    place_id = ""
    user_id = ""
    text = ""
