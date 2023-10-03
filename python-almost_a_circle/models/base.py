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
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_of_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string
        Param Arg: json_string - str rep a list of dicts
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Param Arg: dictionary - double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
