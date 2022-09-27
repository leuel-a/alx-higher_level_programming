#!/usr/bin/python3
"""This is the '11-square' module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is the Square class.

    Square class inherits from the Rectangle class
    """

    def __init__(self, size):
        """Instatiation Methods / Default Constructor

        Args:
            size (int): this is the size of the rectangle
        """
        self.__size = size

    def area(self):
        """Finds the area of the square

        Return:
            int. The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """Overrides the __str__ magic method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
