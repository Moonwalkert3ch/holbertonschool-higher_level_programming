#!/usr/bin/python3
"""Defines a function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """creates an object
    Param Arg: filename - json file"""
    with open(filename) as m:
        return json.load(m)
