#!/usr/bin/python3
"""
3-square Module
"""


class Square:
    """Square Class
    Attributes:
        __size(int): Size of the Square
    """
    def __init__(self, size=0):
        """Instantiation Method / Default Constructor
        Args:
            size(int, optional): Size of the square to be instantiated
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            The area of the Square
        """
        return self.__size ** 2
