#!/usr/bin/python3

'''This module contains the class Review. It encapsulates essential attributes
and methods related a user review (location) '''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Review: represents a user review'''

    place_id = user_id = text = ''
