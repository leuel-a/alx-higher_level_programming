#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -1 * b
        for i in range(1, b):
            a = a * a
        return a
    for i in range(1, b):
        a = a * a
    return a
