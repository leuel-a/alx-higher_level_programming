#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz ", end='')
            continue
        elif i % 5 == 0:
            print("Buzz ", end='')
            continue
        elif i % 15 == 0:
            print("Fizz Buzz ", end='')
            continue
        else:
            print("{} ".format(i), end='')
