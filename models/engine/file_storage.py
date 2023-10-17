#!/usr/bin/python3

"""This module conatins the class for serialization and
deserialization of BaseModel class"""


from models.amenity import Amenity
from models.base_model import BaseModel
import models.base_model
import cmd
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import json
import os


class FileStorage:
    """ serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __objects = {}
    __file_path = "file.json"

    def all(self):
        '''return dictionary of objects: __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''add @obj to __object dict where key = obj_class.id'''
        key = obj.to_dict()['__class__'] + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' serializes @__objects to the JSON file (path: __file_path)'''
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            all_objs = FileStorage.__objects.copy()
            all_obj_dict = {id: obj.to_dict() for id, obj in all_objs.items()}
            file.write(json.dumps(all_obj_dict))

    def reload(self):
        '''deserializes the JSON file to __objects'''
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
            all_reloaded_obj = json.loads(file.read())
            for key, value in all_reloaded_obj.items():
                FileStorage.__objects[key] = globals()[
                    value['__class__']](value)
