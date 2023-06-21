#!/usr/bin/python3
"""defining file storage class for the airbnb project"""
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class DBStorage:
    """file storage class
    attributes: __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialize instances"""
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db)
                                      ,pool_pre_ping=True)
        
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

        #Base.metadata.drop_all(bind=self.__engine)
        
        Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))
        self.__session = Session()

    def all(self, cls=None):
        """query on the current db session
        (self.__session) all objects depending
        of the class name (argument cls)"""
        cls_objs = {"User": User, "State": State, "Amenity": Amenity,
                    "Place": Place, "Review": Review, "City": City}
        objs = {}

        
        for clss in cls_objs:
            if cls == None:
                query = self.__session.query(clss).all()
                for obj in query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objs[key] = obj

        """query = self.__session.query(clss).all()
        for obj in query:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            objs[key] = obj"""
        
        return objs

    def new(self, obj):
        """add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current db session obj if not None"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """create all tables in the db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
