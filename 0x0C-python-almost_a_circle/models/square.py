#!/usr/bin/python3
"""Defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    Attributes:
        __size (int): size of a Square instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation Method / Default Constructor
        Args:
            size (int): size of the new Square instance
            x (int, optional): x position of new Square instance
            y (int, optional): y position of new Square instance
            id (int): id of new Square instance
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of Square instance"""
        return "[Square] <{}> {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for size of Square instance"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size of Square instance"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def update(self, *args, **kwargs):
        """Updates attributes of Square instance
        Args:
            *args (tuple): New attribute values
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs (dict): Key/Value pairs for attributes
        """
        if args is not None and len(args) is not 0:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == "size":
                    setattr(self, "width", v)
                    setattr(self, "height", v)
                else:
                    setattr(self, k, v)
