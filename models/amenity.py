#!/usr/bin/python3

'''This module contains the class Amenity. It encapsulates essential attributes
and methods related an amenity '''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """represents an Amenity"""
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary=place_amenity,  viewonly=False)
