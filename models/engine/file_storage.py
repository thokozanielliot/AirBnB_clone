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


class FileStorage:
    """
    A class that serializes instances to a JSON file &
    deserialize JSON file to instances

    Attributes:
        __file_path: string path to the json file
        __objects: dictionary - empty but will store all objects by class.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj classname>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file"""
        oDict = self.__objects
        objDict = {obj: oDict[obj].to_dict() for obj in oDict.keys()}
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(objDict, f)

    def reload(self):
        """Deserializer the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
