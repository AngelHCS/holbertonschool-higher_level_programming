#!/usr/bin/python3
#3-say_my_name.py
def say_my_name(first_name, last_name=""):
    # Check if first_name and last_name are strings otherwise, typeError
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Print the name
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}" .format(first_name))
