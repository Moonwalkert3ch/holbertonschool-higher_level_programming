#!/usr/bin/python3
"""
Define a function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Param Arg1: obj(any) - instance to check
    Arg2: a_class(same) - specified class
    Returns: True is instance is exact or False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
