#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
and deserializes a JSON file to instances"""



class FileStorage:
    """represents a storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
