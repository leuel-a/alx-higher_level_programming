#!/usr/bin/python3
"""Defines MyList class"""


class MyList(list):
    """This class contains a function that prints a list in a sorted order"""

    def print_sorted(self):
        """Prints elements of a list sorted in an ascending order"""

        sort = self[:]
        for i in range(0, len(self)):
            for j in range(0, len(self) - 1):
                if(sort[j] > sort[j + 1]):
                    temp = sort[j + 1]
                    sort[j + 1] = sort[j]
                    sort[j] = temp

        print(sort)
