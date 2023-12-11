#!/usr/bin/python3

""" This module contains the class BaseModel that defines all common
attributes/methods for other classes (child classes)
"""

import uuid
from datetime import date
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """ defines all common attr/methods for other classes"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        '''initialize instance
           @kwargs: keyworded argument
                each key represents an property name
                each value, the value of the property
        '''
        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        date_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        ignore_attrs = ['__class__', 'created_at', 'updated_at']
        attrs = {key: val for key, val in kwargs.items()
                 if key not in ignore_attrs}
        for key, val in attrs.items():
            setattr(self, key, val)

        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        '''Informal representation of BaseModel object'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update the updated_at attr, with current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        attrs = self.__dict__.copy()
        attrs["__class__"] = self.__class__.__name__
        attrs['created_at'] = attrs['created_at'].isoformat()
        attrs['updated_at'] = attrs['updated_at'].isoformat()
        del attrs["_sa_instance_state"]  # added by sqlalchemy
        return attrs
