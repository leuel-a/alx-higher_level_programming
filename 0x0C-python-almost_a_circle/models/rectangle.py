#!/usr/bin/python3
"""This is the 'rectangle' module"""


from models.base import Base


class Rectangle(Base):
    """This is the 'rectangle' class

    The rectangle class is a child class of the Base class.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        x (optional, int): x axis. Defaults to 0.
        y (optional, int): y axis. Defaults to 0.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation Method / Default Constructor

        Args:
            width (int): width of the new rectangle instance
            height (int): height of the new rectangle instance
            x (optional, int): x axis. Defaults to 0.
            y (optional, int): y axis. Defaults to 0.

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
