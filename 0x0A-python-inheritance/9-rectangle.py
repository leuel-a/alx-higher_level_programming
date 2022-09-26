#!/usr/bin/python3
"""Defines the '9-rectangle' module.

The 9-rectangle module has one class.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is the Rectangle class"""

    def __init__(self, width, height):
        """Instantiation Method / Default Constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Finds the area of the rectangle

        Return:
            int. The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """This is an overide of the __str__ magic method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
