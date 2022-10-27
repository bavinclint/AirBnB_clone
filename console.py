#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""


import cmd

class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb)"
    classes = {
        "Amenity": "Amenity",
        "BaseModel": "BaseModel",
        "City": "City",
        "Place": "Place",
        "Review": "Review",
        "State": "State",
        "User": "User"
    }

    def quit(self, arg):
        """exits the program"""
        return True
    
    def EOF(self, arg):
        """exits the program"""
        return True

    def create(self, arg):
        """creates a new instance of class BaseModel"""

    def show(self, arg):
        """prints the string representation of an instance based on the classname and id"""
    
    def destroy(self, arg):
        """deletes an instance based on the classname and id"""

    def all(self, arg):
        """prints all str representation of all instances based or not on the classname"""

    def update(self, arg):
        """updates an instance based on the classname and id"""

