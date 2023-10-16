#!/usr/bin/python3

'''This module contains the class User. It encapsulates essential attributes
and methods related to user management and interaction within the App'''

from models.base_model import BaseModel


class User(BaseModel):
    '''User class inherits from BaseModel => user of
    The application'''

    first_name = last_name = email = password = ''
