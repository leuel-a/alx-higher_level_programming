#!/usr/bin/python3
"""Defines the State class, an instance of Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Creating the declarative base class
Base = declarative_base()

class State(Base):
    """Class that links to the states table of the hbtn_0e_6_usa DB"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
