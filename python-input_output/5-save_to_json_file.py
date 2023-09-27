#!/usr/bin/python3
"""Defines a function that writes an object to a text file
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an oject to a file
    Param Arg1: my_obj(str) - object to be written 
    Arg2: filename(str) - file
    """
    with open(filename, "w") as m:
        json.dump(my_obj, m)
