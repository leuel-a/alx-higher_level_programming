#!/usr/bin/python3
"""This is the '6-load_from_json_file' module."""


def load_from_json_file(filename):
    """Creates an Object (Python Object) from a JSON file

    Args:
        filename: file containing a JSON document

    """

    import json

    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)

    return data
