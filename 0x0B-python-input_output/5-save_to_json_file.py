#!/usr/bin/python3
"""This is the '5-save_to_json_file' module"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using JSON representation.

    Args:
        my_obj: the object that will be written
        filename: the file that will be written to
    """

    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
