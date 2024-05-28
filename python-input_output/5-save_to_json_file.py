#!/usr/bin/python3
# 5-save_to_json_file.py
""" Write object to text file using json represantation"""


import json


def save_to_json_file(my_obj, filename):
    """defining function"""

    with open(filename, 'w') as f:
        try:
            json.dump(my_obj, f)
        except TypeError:
            raise TypeError("Object of type set is not JSON serializable")
