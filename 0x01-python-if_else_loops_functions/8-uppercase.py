#!/usr/bin/python3
new = ''
def uppercase(str):
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            new = new + chr((ord(i) - 32))
        else:
            new = new + i
print("{}".format(new))
