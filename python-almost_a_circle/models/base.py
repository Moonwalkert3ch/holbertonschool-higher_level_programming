#!/usr/bin/python3
"""Defines a Base class model"""
import json


class Base:
    """Represents a Base model
    Attr: __nb_objects(int) - counter
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes base

        Param arg: id(int) - identity of base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Param Arg: list_dictionaries - list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
