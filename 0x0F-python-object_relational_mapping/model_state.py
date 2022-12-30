#!/usr/bin/python3
"""Defines the State class, an instance of Base = declarative_base()"""
from sys import argv as av
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

# Creating the declarative base class
Base = declarative_base()

class State(Base):
    """Class that links to the states table of the hbtn_0e_6_usa DB"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Create the engine for the connection
connection_url = sqlalchemy.engine.URL.create(
    drivername="mysql+mysqldb",
    username=av[1],
    password=av[2],
    database=av[3],
    host="localhost",
    port=3306
)
Engine = create_engine(connection_url)
Base.metadata.create_all(Engine)
