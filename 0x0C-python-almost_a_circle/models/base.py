#!/usr/bin/python3
"""Defines the `base` class"""


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
