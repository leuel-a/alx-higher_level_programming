#!/usr/bin/python3
"""This is the 'square' module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class

    Attributes:
        size (int): the size of the square
        x (int): the x position of the square
        y (int): the y position of the square

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation Constructor / Default Constructor

        Args:
            size (int): the size of the square
            x (optional, int): the x position of the square.
                Defaults to 0.
            y (optional, int): the y position of the square
                Defaults to 0.
            id (optional, int): the id of the square instance

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloaded magic method __str__

        Returns:
            str: the sring representation of the square instance

        """
        return "[Square] ({})".format(self.id) +\
            " {}/{} - ".format(self.x, self.y) +\
            "{}".format(self.width)
