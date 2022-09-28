#!/usr/bin/python3
"""This is the '3-to_json_string' module.

The 3-to_json_string module has one function.
"""


def to_json_string(my_obj):
    """Serializes an object to JSON string.

    Args:
        my_obj: this is the object to be serialized

    Returns:
        str. The JSON representation of an object.
    """

    import json

    return json.dumps(my_obj)
