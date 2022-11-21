#!/usr/bin/python3
"""Defines the `text_indentation` function"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in range(0, len(text)):
        if (text[i - 1] in ['.', '?', ':']):
            print("\n")
            i += 1
        else:
            print(text[i], end="")

    print()