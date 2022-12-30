#!/usr/bin/python3
"""Defines the State class, an instance of Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from urllib.parse import quote

# Creating the declarative base class
Base = declarative_base()

class State(Base):
    """Class that links to the states table of the hbtn_0e_6_usa DB"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Create the engine for the connection
user, passwd, host, port, db = 'root', 'la@1993#', 'localhost', 3306, 'hbtn_0e_6_usa'
Engine = create_engine(f"mysql+mysqldb://{user}:{quote(passwd)}@{host}:{port}/{db}")
Base.metadata.create_all(Engine)
