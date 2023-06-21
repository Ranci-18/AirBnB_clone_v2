#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Amenity(BaseModel, Base):
    name = Column(String(128), nullable=False)

    def __init__ = 'amenities'
    super().__init__(*args, **kwargs)
