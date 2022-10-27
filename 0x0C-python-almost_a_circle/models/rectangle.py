#!/usr/bin/python3
"""Defines the `Rectangle class`"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class that inherits from Base
    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
        __x (int): x position of the rectangle
        __y (int): y position of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation Method / Default Constructor
        Args:
            width (int): width of a new rectangle instance
            height (int): height of a new rectangle instance
            x (int, optional): x position of the rectangle instance.
                Defaults to 0.
            y (int, optional): y position of the rectangle instance.
                Defaults to 0.
            id (int): id of the rectangle instance
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width of Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width of Rectangle instance"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height of Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height of Rectangle instance"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter for x of Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x of Rectangle instance"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for y of Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y of Rectangle instance"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Finds the area of a Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance to the stdout"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end='')
            for j in range(0, self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """String representation of rectangle object"""
        return "[Rectangle] ({}) {}/{} -" \
               " {}/{}".format(self.id, self.__x,
                               self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update a Rectangle instance
        Args:
            *args (tuple): New attribute values
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs (dict): Key/Value pairs for attributes
        """
        if args is not None and len(args) is not 0:
            attr = ["width", "height", "x", "y", "id"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
