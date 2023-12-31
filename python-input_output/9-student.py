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

    def to_json(self):
        """Retrieves the dictionary representation"""
        return self.__dict__
