#!/usr/bin/python3
"""Defines a function that adds 2 integers """


def add_integer(a, b=98):
    """ Returns the addition of a and b
    Param arg1: a - first integer
    arg2: b - second integer
    raises exceptions:
    TypeError - if not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
