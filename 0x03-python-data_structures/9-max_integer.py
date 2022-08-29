#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_in_list = 0
        for i in range(0, len(my_list)):
            if max_in_list < my_list[i]:
                max_in_list = my_list[i]
        return max_in_list
    return None
