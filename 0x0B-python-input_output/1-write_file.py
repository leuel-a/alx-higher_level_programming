#!/usr/bin/python3
"""This is the '1-read_file' module.

The 1-write_file has one function.
"""


def write_file(filename="", text=""):
    """Writes a text to the file that is specified.

    Args:
        filename (str): this is the file to be written to,
            and if the file does not exist it will be created

        text (str): this is the text that will be written

    Return:
        int. The number of characters that will be written.
    """

    with open(filename, 'w+', encoding="utf-8") as f:
        num_of_char = f.write(text)

    return num_of_char
