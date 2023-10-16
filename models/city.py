#!/usr/bin/python3

'''This module contains the class City. It encapsulates essential attributes
and methods related a City (location) '''

from models.base_model import BaseModel


class City(BaseModel):
    '''City: represents an actual City'''

    state_id = ''
    name = ''
