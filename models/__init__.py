#!/usr/bin/python3
"""Create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()