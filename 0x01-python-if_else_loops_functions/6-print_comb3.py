#!/usr/bin/python3
for x in range(0, 9):
    for y in range(0, 9):
        if (x < y):
            print("{}{}, ".format(x, y), end='')
print("{}{}".format(8, 9))
