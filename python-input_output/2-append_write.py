#!/usr/bin/python3
# 2-append_write.py

def append_write(filename="", text=""):
    """Append text to a file and return chars added"""

    with open(filename, mode='a', encoding='utf-8') as file:
        """Open where the file is using the encoding"""

        file.write(text)
        """Put the text in the file"""

        return len(text)
    """Return the chars added"""
