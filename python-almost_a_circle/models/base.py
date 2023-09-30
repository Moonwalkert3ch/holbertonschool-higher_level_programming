#!/usr/bin/python3
"""Defines a Base class model"""


class Base:
    """Represents a Base model
    Attr: __nb_objects(int) - count
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
            Base.__no_objects += 1
            self.id = Base.__nb_objects
