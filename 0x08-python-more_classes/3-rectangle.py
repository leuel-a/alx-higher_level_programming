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

    def area(self):
        """
        Finds the area of the rectangle

        Return:
            int. Area of the rectangle
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """
        Finds the perimeter of the rectangle

        Return:
            int. Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = 2 * (self.__width + self.__height)
            return perimeter

    def __str__(self):
        """
        Prints the rectangle with # character.
        Return:
            string. String representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lr = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                lr.append('#')
            lr.append('\n')
        return ("".join(lr))
