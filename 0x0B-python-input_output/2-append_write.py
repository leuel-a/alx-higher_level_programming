#!/usr/bin/python3
"""This is the '2-append_write' module.

The 2-append_write has one function.
"""


def append_write(filename="", text=""):
    """Appends a text to the end of a text file.

    Args:
        filename (str): this is the file to be appended
        text (str): this is the text to be written

    Description:
        If the file is not found, or does not exist, then
            file will be created

    Return:
        int. The number of characters added to the file.
    """

    with open(filename, 'a+', encoding="utf-8") as f:
        num_of_char = f.write(text)

    return num_of_char
