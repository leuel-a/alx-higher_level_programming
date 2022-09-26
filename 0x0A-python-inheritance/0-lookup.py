#!/usr/bin/python3
"""Defines the lookup function"""


def lookup(obj):
    """Finds a list of objects for the given object"""

    object_list = []
    for i in dir(obj):
        object_list.append(i)
    return object_list
