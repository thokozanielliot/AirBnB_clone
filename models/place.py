#!/usr/bin/python3
"""Define a Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represent a Place class

    Attributes:
        city_id(string): Will be City.id
        user_id(String): Will be User.id
        name(string)
        description(string)
        number_rooms(integer)
        number_bathrooms(integer)
        max_guest(integer)
        priceS_by_night(integer)
        latitude(float)
        longitude(float)
        amenity_ids(list): Will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __int__(self, *args, **kwargs):
        """Initializes Place"""
        super().__init__(*args, **kwargs)
