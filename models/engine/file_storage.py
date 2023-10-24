#!/usr/bin/python3
"""This is File Storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State

allClasses = {"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
           "City": City, "Place": Place, "Review": Review, "State": State}


class FileStorage:
    """
    Serialize instances to a JSon file & Deserializes back to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file"""
        jsonObjects = {}
        for key in self.__objects:
            jsonObjects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(jsonObjects, f)
    
    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                jsonObjects = json.load(f)
            for key in jsonObjects:
                self.__objects[key] = allClasses[jsonObjects[key]["__class__"]](**jsonObjects[key])
        except FileNotFoundError:
            pass
