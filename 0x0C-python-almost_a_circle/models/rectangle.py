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
        self.__width = width

    @property
    def height(self):
        """Getter for height of Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height of Rectangle instance"""
        self.__height = height

    @property
    def x(self):
        """Getter for x of Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x of Rectangle instance"""
        self.__x = x

    @property
    def y(self):
        """Getter for y of Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y of Rectangle instance"""
        self.__y = y
