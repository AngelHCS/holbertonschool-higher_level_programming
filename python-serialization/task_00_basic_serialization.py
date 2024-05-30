#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """Serialize the py dict 'data' to a JSON file specified by 'filename'."""

    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from the file to a dictionary."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
