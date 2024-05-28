#!/usr/bin/python3
# 1-write_file.py
"""
Function writes a string to text file
"""


def write_file(filename="", text=""):
    """ defines the function """
    with open(filename, 'w', encoding='utf-8') as f:
        """ uses UTF8 to write string to text file """
        return f.write(text)
