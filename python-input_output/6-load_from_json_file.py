#!/usr/bin/python3
# 6-load_from_json_file.py
""" Loads Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """definition"""

    with open(filename, 'r') as f:
        return json.load(f)
