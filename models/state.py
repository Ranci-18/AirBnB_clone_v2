#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ



class State(BaseModel, Base):
    """ State class """
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship('City', cascade='all, delete-orphan',
                               backref='state', passive_deletes=True)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        def cities(self):
            """getter method returns list of city instances"""
            from models import storage
            city_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
