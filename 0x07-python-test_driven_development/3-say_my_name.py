#!/usr/bin/python3
"""Defines the `say_my_name` function"""


def say_my_name(first_name, last_name=""):
    """Prints full name to stdout
    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to an empty string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
