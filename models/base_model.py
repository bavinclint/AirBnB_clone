#!/usr/bin/python3
"""Class BaseModel that defines all common attributes/methods
for other classes"""


from datetime import datetime
import models
import uuid


class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """initializing public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        dformat =  "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """return string representation of instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """the public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save(self)
    
    def to_dict(self):
        """returns a dict containing all keys/values of __dict__ of instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
