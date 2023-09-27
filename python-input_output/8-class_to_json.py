#!/usr/bin/python3
"""Defines a function that returns the ditionary description of an object"""


def class_to_json(obj):
    """
    Param Arg: object - an instance of a class
    Returns: dictionary
    """
    return obj.__dict__
