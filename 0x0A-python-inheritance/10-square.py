#!/usr/bi/python3
"""This module has one class, Square class.

The Square class inherit from the 9-rectangle module.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is the Square class"""

    def __init__(self, size):
        """Instatiation Method / Default Constructor

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
