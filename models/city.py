#!/usr/bin/python3

'''This module contains the class City. It encapsulates essential attributes
and methods related a City (location) '''

from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="city",
                              cascade="all, delete-orphan")
