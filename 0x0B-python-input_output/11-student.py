#!/usr/bin/python3
"""This is the '11-student' module"""


class Student:
    """This is the Student class

    Attributes:
        first_name: the first name of the student
        last_name: the lat name of the student
        age: the age of the student

    """

    def __init__(self, first_name, last_name, age):
        """Instantiation Method / Default Constructor

        Args:
            first_name (str): first name of the new student
            last_name (str): last name of the new student
            age: age of the new student

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

    def reload_from_json(self, json):
        """Replaces all attributes of a student instance

        Args:
            json (dict): dictionary representation of the new
                attributes that the student instance will assume

        """
        for k, v in json.items():
            setattr(self, k, v)
