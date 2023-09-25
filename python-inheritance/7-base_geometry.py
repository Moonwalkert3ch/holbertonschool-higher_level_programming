i#!/usr/bin/python3
"""Defines a base geometry class """


class BaseGeometry:
    """Represents base geometry """

    def area(self):
        """Not implemented yet
        Raises: Exception message due to no implementation"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validates value as an integer
        Param: Arg1: name(str) - string
        Arg2: value(int) - parameter to be validated
        Raises: TypeError if not integer
        ValueError if lt 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError({"{} must be greater than 0".format(name))
