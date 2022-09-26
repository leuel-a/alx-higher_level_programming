#!/usr/bin/python3
"""Defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of the specified class

    Args:
        obj: the object to be checked
        a_class: the class to be refrenced

    Return:
        True, if the object is exactly an instance of the specified class.
        Otherwise, it returns false.
    """
    
    if (type(obj) == a_class):
            return True
    return False
