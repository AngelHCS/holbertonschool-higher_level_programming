#!/usr/bin/python3
# 0-read_file.py

"""reads file and prints it to stdout"""


def read_file(filename=""):

    """
    Read the contents of a text file and print them to stdout

    Args:
    filename (str): The name of the file to be read.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
