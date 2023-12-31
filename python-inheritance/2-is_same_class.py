#!/usr/bin/python3
"""Defines a function that returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
     Param: Arg1: obj(any) - instancee to check
     Arg2: a_class(match1) - specified class
     returns True if the object is exactly an instance
     otherwise flse if not of the specified class
    """
    if type(obj) == a_class:
        return True
    return False
