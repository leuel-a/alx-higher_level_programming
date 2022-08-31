#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_2 = a_dictionary.copy()
    for x in a_dictionary_2.keys():
        a_dictionary_2[x] *= 2
    return (a_dictionary_2)
