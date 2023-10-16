#!/usr/bin/python3

"""This module conatins the class for serialization and
deserialization of BaseModel class"""


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        ''' serializes @__objects to the JSON file (path: __file_path)'''
        with open(FileStorage.___file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        '''deserializes the JSON file to __objects'''
        if not os.path.exists(FileStorage.___file_path):
            return
        with open(FileStorage.___file_path, 'r', encoding='utf-8') as file:
            FileStorage.__objects = json.loads(file.read())
