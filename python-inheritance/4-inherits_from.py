#!/usr/bin/python3
"""
Defines a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Param Arg1: obj(any) - instance to be checked
    Arg2: a_class(same) - specified class
    Returns: True if instance found otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
