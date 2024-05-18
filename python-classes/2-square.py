#!/usr/bin/python3#!/usr/bin/python3
# 2-square.py

"""Define a class called Square."""


class Square:
    """Represent the square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
