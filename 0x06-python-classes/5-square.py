#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square Class
    Attributes:
        __size: Size of the square
    """
    def __init__(self, size=0):
        """Instantiation Methoo / Default Constructor
        :param size: Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for the __size Attribute
        :return: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the __size Attribute
        :param value: Value that will become the new value of __size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Finds the Area of the Square
        :return: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()
