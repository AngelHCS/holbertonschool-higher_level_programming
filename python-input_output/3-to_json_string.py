#!/usr/bin/python3
# 3-to_json_string.py
"""function that returns the json representation of an object"""
import json


def to_json_string(my_obj):
    """return a string that is the json represation of an obj"""
    return json.dumps(my_obj)
