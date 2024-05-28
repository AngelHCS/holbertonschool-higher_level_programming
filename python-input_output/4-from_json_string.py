#!/usr/bin/python3
# 4-from_json_string.py


"""Returns a Python object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Defines the function, has the argument of my_str"""
    return json.loads(my_str)
