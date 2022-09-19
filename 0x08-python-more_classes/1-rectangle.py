#!/usr/bin/python3
"""
    This is the "1-rectangle" module.

    The 1-rectangle module supplies one class. This class
    defines a rectangle
"""

class Rectangle:
    """
        This is the Rectangle class
        Attritbutes:
            __width: Width of rectangle
            __height: Height of rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Instantiation methods / Constructor

            Args:
                @width: Width of rectangle
                @height: Height of rectangle
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """
        Getter for the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle
        
        Args:
            @value: Value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height

        Args:
            @value: Value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
