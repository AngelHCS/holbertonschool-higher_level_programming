#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError):  # wants me to specify the error for return
        return False
