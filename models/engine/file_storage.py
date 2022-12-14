#!/usr/bin/python3

"""

This module defines a FileStorage Class

"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    A FileStorage class
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj: BaseModel):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            objects = {key: value.to_dict()
                       for key, value in self.__objects.items()}
            f.write(json.dumps(objects))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_object = json.loads(f.read())

                objects = {}

                for key, value in json_object.items():
                    model_name = key.split('.')[0]
                    if model_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif model_name == 'User':
                        obj = User(**value)
                    elif model_name == 'State':
                        obj = State(**value)
                    elif model_name == 'City':
                        obj = City(**value)
                    elif model_name == 'Amenity':
                        obj = Amenity(**value)
                    elif model_name == 'Place':
                        obj = Place(**value)
                    else:
                        obj = Review(**value)

                    objects[key] = obj

                self.__objects = objects
