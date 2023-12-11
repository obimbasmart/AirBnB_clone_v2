#!/usr/bin/python3

'''This module contains the class User. It encapsulates essential attributes
and methods related to user management and interaction within the App'''

from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''User class inherits from BaseModel => user of
    The application'''

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
