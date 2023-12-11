#!/usr/bin/python3

"""
'''This module contains the class Place. It encapsulates essential attributes
and methods related a Place (location) '''
"""

from models.base_model import BaseModel, Base
from models.review import Review
from os import environ
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity",
                      Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id")),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id")))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        user = relationship("User", back_populates="places")
        city = relationship("City", back_populates="places")
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="amenities",
                                 viewonly=False)

    @property
    def reviews(self):
        """ returns the list of reviews instances with
        place_id equals to the current place.id"""
        from models import storage
        return [review for review in storage.all(Review).values()
                if self.id == review.place_id]
