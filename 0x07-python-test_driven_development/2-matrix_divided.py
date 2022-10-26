#!/usr/bin/python3
"""Defines the 'matrix_divided' function"""


def matrix_divided(matrix, div):
    """Returns the division of a matrix by div
    Args:
        matrix (list): the matrix to be divided
        div (int, float): the divisor to the matrix
    Returns:
        (list): a new matrix with the result of the division
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    new_matrix = []
    for row in matrix:
        sub_list = []
        for i in row:
            sub_list.append(round(i / div, 2))
        new_matrix.append(sub_list)
    return new_matrix
