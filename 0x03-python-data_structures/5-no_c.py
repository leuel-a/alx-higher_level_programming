#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new = ''
    for i in range(0, len(my_string)):
        if (my_string[i] == 'c') or (my_string[i] == 'C'):
            continue
        new = new + my_string[i]
    return (new)
