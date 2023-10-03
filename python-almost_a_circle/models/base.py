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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Param Arg1: list_objs - list of inheritance instances in base
        """
    if list_objs is None:
        with open(f"{cls.__name__}.json", "w+",) as jfile:
            json.dump([], jfile)
            return

        dict_list = []
        for instance in list_objs:
            instance_list = cls.to_dictionary(instance)
            dict_list.append(instance_list)

        jlist = Base.to_json_string(dict_list)

        with open(f"{cls.__name__}.json", "w+") as jfile:
            f.write(jlist)
