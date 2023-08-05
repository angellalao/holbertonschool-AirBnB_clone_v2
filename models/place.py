#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", back_populates='place',
            cascade="all, delete, delete-orphan")

    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")

"""
    @property
    def reviews(self):
        return the list of Review instances that belong to the place
        from models import storage
        review_dict = storage.all(Review)
        review_list = []
        for key, val in review_dict.items():
            if self.id == val.place_id:
                review_list[key] = val
        return review_list
"""
