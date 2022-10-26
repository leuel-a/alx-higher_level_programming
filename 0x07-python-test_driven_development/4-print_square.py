#!/usr/bin/python3
"""Defines the ``print_square`` function"""


def print_square(size):
    """Prints a square of specified size with '#'
        character to stdout
    Args:
        size (int): size of the square to be printed
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
