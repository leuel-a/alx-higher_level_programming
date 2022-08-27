#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = my_list
    for i in range(0, len(a)):
        print(f"{a[i]}".format(a[i]))
