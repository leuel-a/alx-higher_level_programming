#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    bool_val = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        bool_val = False
    finally:
        return bool_val
