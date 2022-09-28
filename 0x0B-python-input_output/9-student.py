#!/usr/bin/python3
"""This is the '9-student' module"""


class Student:
    """This is the Student class.

    Attributes:
        first_name: first name of the student
        last_name: last name of the student
        age: age of the student
    """

    def __init__(self, first_name, last_name, age):
        """Instantitation Method / Default Constructor

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a
        Student instance."""
        return self.__dict__
