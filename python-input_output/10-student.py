#!/usr/bin/python3
"""Defines a class student by its attributes """


class Student:
    """Represents class student"""

    def __init__(self, first_name, last_name, age):
        """initiliazes student class
        Param arg1: first_name - student first name
        arg2: last_name - student last name
        arg3: age - student age
        Returns: dictionary representation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation
        Param Arg: attrs(str) - retrieve attr names """
        if (type(attrs) == list and
                all(type(chars) == str for chars in attrs)):
            return {names: getattr(self, names) for names in attrs
                    if hasattr(self, names)}
        return self.__dict__
