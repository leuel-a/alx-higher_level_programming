#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        column = []
        for j in range(0, len(matrix[i])):
            column.append((matrix[i][j]) * (matrix[i][j]))
        new_matrix.append(column)
    return (new_matrix)
