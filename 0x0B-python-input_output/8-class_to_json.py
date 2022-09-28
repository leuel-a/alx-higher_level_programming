#!/usr/bin/python3
"""This is the '8-class_to_json' module."""


def class_to_json(obj):
    """Returns the dictionary description for JSON
    serialiazation of an object.

    Args:
        obj: the object to be parsed

    Return:
        dic. A dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
        serialization of an object.
    """

    return obj.__dict__
