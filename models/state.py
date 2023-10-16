#!/usr/bin/python3

'''This module contains the class State. It encapsulates essential attributes
and methods related a State (location) '''

from models.base_model import BaseModel


class State(BaseModel):
    '''State: represents an actual state'''

    state_id = ''
    name = ''
