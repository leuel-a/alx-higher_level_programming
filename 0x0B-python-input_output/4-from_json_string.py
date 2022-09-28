#!/usr/bin/python3
"""This is the '4-from_json_string' module.

The 4-from_json_string has one function.
"""


def from_json_string(my_str):
    """Decodes a JSON string to python representation.

    Args:
        my_str (str): the string that will be decoded

    Return:
        obj. Python data structure of the string
    """

    import json

    return json.loads(my_str)
