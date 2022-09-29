#!/usr/bin/python3
"""This is the '10-square' module"""


class Student:
    """This is the student class

    Attributes:
        first_name: this is the first name of th student
        lasy_name: this is the last name of the student
        age: this is the age of the student

    """

    def __init__(self, first_name, last_name, age):
        """Instantiation Method / Default Constructor

        Args:
            first_name (str): first name of the new student
            last_name (str): last name of the new student
            age (int): age of the new student

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the student
        instance.

        Args:
            attrs (list): this limits the data that will be retrieved
                in the dictionary representation

        Description:
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved.

        """
        if attrs is None:
            return self.__dict__
        Dict = {}
        for i in self.__dict__:
            for j in attrs:
                if i == j:
                    Dict[j] = self.__dict__[i]

        return Dict
