#!/usr/bin/python3
"""Defines a Rectangle clss that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry'). BaseGeometry


class Rectangle(BaseGeometry):
    """"Represents a BaseGeometry rectangle"""

    def __init__(self, width, height):
        """
        Initializes Rectangle class

        Param Arg1: width(int) - width of rectangle
        Arg2: height(int) - height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
