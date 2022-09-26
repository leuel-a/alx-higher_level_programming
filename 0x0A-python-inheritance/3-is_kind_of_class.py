#!/usr/bin/python3
"""Defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
        obj: this is the object to be checked
        a_class: the class to be checked

    Return:
        bool. True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified
        class. Otherwise False
    """

    if (isinstance(obj, a_class)):
        return True
    return False
