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

    @property
    def size(self):
        """Getter for the size attribute

        Return:
            int: the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """Setter for the size of square instance

        Args:
            size (int): the size of the square

        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates attributes of a given object

        Args:
            *args: this are arguments that will assume the new attributes
                - args[0] (int) - the new id
                - args[1] (int) - the new size
                - args[2] (int) - the x position
                - args[3] (int) - the y position
            **kwargs: these are new key value pairs that will assume the
                attributes of the square instance

        """
        if (args and len(args) != 0):
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                    self.height = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        elif kwargs:
            for attributes, value in kwargs.items():
                if hasattr(self, attributes):
                    setattr(self, attributes, value)

    def to_dictionary(self):
        """Returns a dictionary representation of Square instance"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}
