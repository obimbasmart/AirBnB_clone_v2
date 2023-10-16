#!/usr/bin/python3

'''This module contains the class Place. It encapsulates essential attributes
and methods related a Place (location) '''

from models.base_model import BaseModel


class Place(BaseModel):
    '''Place: represents an actual place'''

    city_id = user_id = name = description = ''

    number_rooms = number_bathrooms = max_guest = price_by_night = 0

    latitude = longitude = 0.0
    amenity_id = []
