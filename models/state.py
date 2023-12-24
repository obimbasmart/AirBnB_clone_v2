#!/usr/bin/python3

'''This module contains the class State. It encapsulates essential attributes
and methods related a State (location) '''

from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    '''State: represents an actual state'''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """ returns the list of City instances with
            state_id equals to the current State.id"""
            from models import storage
            return [city for city in storage.all(City).values()
                    if self.id == city.state_id]
