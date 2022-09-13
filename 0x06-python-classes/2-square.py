#!/usr/bin/python3
"""2-square Module"""


class Square:
    """Square Class
    Attributes:
        __size(int): Size of the square
    """

    def __init__(self, size=0):
        """Initialization Method / Default Constructor
        Args:
            size: Size of the square to be instantiated
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
