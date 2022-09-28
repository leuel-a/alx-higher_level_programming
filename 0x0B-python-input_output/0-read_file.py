#!/usr/bin/python3
"""This is the "0-read_file" module.

The 0-read_file module has one function, read_file
"""


def read_file(filename=""):
    """Reads a file specified and print to the stdout

    Args:
        filename (str): the name of the file to be read
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end='')
