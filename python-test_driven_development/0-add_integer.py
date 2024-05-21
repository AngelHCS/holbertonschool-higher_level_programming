#!/usr/bin/python3
# 0-add_integer.py

"""int addition function."""


def add_integer(a, b=98):
    """Return the int addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-int and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an int")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an int")
    return (int(a) + int(b))
