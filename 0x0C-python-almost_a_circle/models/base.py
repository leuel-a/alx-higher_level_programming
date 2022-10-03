#!/usr/bin/python3
"""This is the 'base' module"""


import json


class Base:
    """This is the Base class

    Attributes:
        nb_objects (int): the number of objects instatiated from
            the base class

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation Method / Default Constructor

        Args:
            id (optional, int): the id of the new object

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict): list of dictionaries

        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
