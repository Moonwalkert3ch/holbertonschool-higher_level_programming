#!/usr/bin/python3
"""Defines a function that returns the JSON
representation of a string object"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    Param Arg: my_obj(str) - string object
    """
    return json.dumps(my_obj)
