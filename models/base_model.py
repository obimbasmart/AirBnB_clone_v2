#!/usr/bin/python3

""" This module contains the class BaseModel that defines all common
attributes/methods for other classes (child classes)
"""

import uuid
from datetime import date
from datetime import datetime
from models import storage


class BaseModel:
    """ defines all common attr/methods for other classes"""

    def __init__(self, *args, **kwargs):
        '''initialize instance
           @kwargs: keyworded argument
                each key represents an property name
                each value, the value of the property
        '''
        if len(kwargs):
            self.__init(**kwargs)
            return

        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        storage.new(self)

    def __init(self, **kwargs):
        """initialize instance attributes using kwargs
        @kwargs: dictionary of key, value for each attribute
        """
        for key, value in kwargs.items():
            if (key == "__class__"):
                continue
            if (key in 'created_at | updated_at'):
                setattr(self, key, datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f'))
                continue

            setattr(self, key, value)

    def __str__(self):
        '''Informal representation of BaseModel object'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update the updated_at attr, with current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        attrs = self.__dict__.copy()
        attrs["__class__"] = self.__class__.__name__
        attrs['created_at'] = attrs['created_at'].isoformat()
        attrs['updated_at'] = attrs['updated_at'].isoformat()
        return attrs
