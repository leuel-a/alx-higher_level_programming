#!/usr/bin/python3
"""Defines the `base` class"""
import json


class Base:
    """Base for all other classes in this project
    Attributes:
        __nb_objects (int): the number of objects created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation Method / Default Constructor
        Args:
            id (int, optional): identifier for objects. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of `list_objs` to a file
        Args:
            list_objs (list): list of instances who inherits from Base
        """
        list_dicts = []
        for instance in list_objs:
            list_dicts.append(instance.to_dictionary())
        json_str = Base.to_json_string(list_dicts)

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)
