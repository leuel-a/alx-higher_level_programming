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
        filename = cls.__name__ + ".json"

        list_dicts = []
        if list_objs is not None:
            for instance in list_objs:
                list_dicts.append(json.loads(cls.to_json_string(
                    instance.to_dictionary()
                )))

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(list_dicts, f)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation `json_string`"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
