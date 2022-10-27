#!/usr/bin/python3
"""Defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    Attributes:
        id (int): id of a Square instance
        size (int): size of a Square instance
        x (int): x position of a Square instance
        y (int): y position of a Square instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation Method / Default Constructor
        Args:
            size (int): size of the new Square instance
            x (int, optional): x position of new Square instance
            y (int, optional): y position of new Square instance
            id (int): id of new Square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of Square instance"""
        return "[Square] <{}> {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
