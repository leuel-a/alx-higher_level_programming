#!/usr/bin/python3
"""Defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified
    class.

    Args:
        obj: the object to be checked
        a_class: the class to be checked

    Return:
        bool. True if the object is an instance of, or if
        the object is an instance of a class that inherited
        from, the specified class. Otherwise False.
    """

    if (issubclass(type(obj), a_class)) and type(obj) != a_class:
        return True
    return False
