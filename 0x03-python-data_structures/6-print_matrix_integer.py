#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j == 0:
                print("{:d}".format(matrix[i][j]), end='')
            else:
                print(" {:d}".format(matrix[i][j]), end='')
        print()
