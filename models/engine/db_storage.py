#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """create engine and session for db storage"""
        self.__engine = \
            create_engine('mysql+mysqldb://{}:{}@{}/{}'
                          .format(os.environ.get("HBNB_MYSQL_USER"),
                                  os.environ.get("HBNB_MYSQL_PWD"),
                                  os.environ.get(
                              "HBNB_MYSQL_HOST"),
                              os.environ.get("HBNB_MYSQL_DB")),
                          pool_pre_ping=True)

    def all(self, cls=None):
        """Returns a dictionary of objects currently in database"""
        all_models = [State, City, User, Place, Review]
        if cls is None:
            all_objects = {}
            for klass in all_models:
                klass_objects = self.__session.query(klass).all()
                all_objects.update({obj.__class__.__name__ + '.' +
                                    obj.id: obj for obj in klass_objects})
            return all_objects

        return {obj.__class__.__name__ + '.' + obj.id:
                obj for obj in self.__session.query(cls).all()}

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """delete @obj from the current database session"""
        if obj:
            del obj

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
