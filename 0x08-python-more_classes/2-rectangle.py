#!usr/bin/python3
"""
    This is the "2-rectangle" module.

    The 2-rectangle module defines one class. This class defines
    a rectangle
"""


class Rectangle:
    """
    This is the Rectangle class.
    
    Attributes:
        __width: Width of the rectangle
        __height: Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation method / Constructor
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Getter for the width.
        
        Return:
            int. Width of the rectangle.
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Setter for the width.
        
        Args:
            value (int): Value for the width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """
        Getter for the height.
        
        Return:
            int. Height of the rectangle.
        """
    @height.setter
    def height(self, value):
        """
        Setter for the height.
        Args:
            value (int): Value for the height
        """
        self.__height = value
    def area(self):
        """
        Finds the area of the rectangle.

        Return:
            int. Area of the rectangle
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        Finds the perimeter of the rectangle

        Return:
            int. Perimeter of the rectangle.
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            perimeter = 2 * (self.__width + self.__height)
            return perimeter
        
