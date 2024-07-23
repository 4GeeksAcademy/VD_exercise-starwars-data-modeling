import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50),nullable=False)
    email = Column(String(150),nullable=False)
    password= Column(String(50),nullable=False)
    date_of_suscription= Column(Date,nullable=False)
    favorites = relationship('Favorite', backref='user', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_favorite = Column(Integer, primary_key=True)
    name = Column(String (50))
    user_id = Column(Integer, ForeignKey('user.id_user'))
    planet_id= Column(Integer, ForeignKey('planet.id_planet'))
    character_id= Column(Integer, ForeignKey('character.id_character'))
    vehicle_id= Column(Integer, ForeignKey('vehicle.id_vehicle'))
    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_planet = Column(Integer, primary_key=True)
    name = Column(String (50))
    population = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    favorites= relationship('Favorite', backref='planet', lazy=True)
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_vehicle = Column(Integer, primary_key=True)
    name = Column(String (50), nullable=False)
    model = Column(String(50), nullable=False)
    size = Column(Integer, nullable=False)
    favorites= relationship('Favorite', backref='vehicle', lazy=True)
    
class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_character = Column(Integer, primary_key=True)
    name = Column(String (50))
    gender = Column(Integer, nullable=False)
    eye = Column(Integer, nullable=False)
    favorites= relationship('Favorite', backref='character', lazy=True)

    
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
