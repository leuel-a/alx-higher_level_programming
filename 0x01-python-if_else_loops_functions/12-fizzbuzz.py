#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 15 == 0:
            print("Fizz ", end='')
        elif i % 3 == 0:
            print("Buzz ", end='')
        elif i % 5:
            print("Fizz Buzz ", end='')
        else:
            print("{} ".format(i), end='')