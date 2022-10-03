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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: is a list of instances who inherits of 'Base'

        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = []
                for i in list_objs:
                    list_dictionaries.append(i.to_dictionary())
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries

        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary (dict): can be thought of as a double
                pointer to a dictionary

        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
