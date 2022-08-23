#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        b = -1 * b
        for i in range(1, (b+1)):
            a = a / a
        return a
    for i in range(1, b):
        a = a * a
    return a
