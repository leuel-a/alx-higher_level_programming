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

    @property
    def width(self):
        """Getter for the width of the instance

        Returns:
            int: the width of the instance
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for the width of the instance

        Args:
            width (int): width of the instance
        """
        self.__width = width

    @property
    def height(self):
        """Getter for the height of the instance

        Returns:
            int: the height of the instance
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for the height of the instance

        Args:
            height (int): height of the instance

        """
        self.__height = height

    @property
    def x(self):
        """Getter for the x attribute of the instance

        Returns:
            int: the x attribute of the instance
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for the x attribute of the instance

        Args:
            int: the x attribute of the instance

        """
        self.__x = x

    @property
    def y(self):
        """Getter for the y attribute of instance

        Returns:
            int: the y attribute of the instance
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for the y attribute of instance

        Args:
            int: the y attribute of instance

        """
        self.__y = y
