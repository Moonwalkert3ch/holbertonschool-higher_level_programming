#!/usr/bin/python3
"""Defines a class Rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle
        Param Arg1: width - width of rectangle
        Arg2: height - height of rectangle
        Arg3: x - points to itself
        Arg4: y - points to itself
        Arg5: id - none
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y =y

    @property
    def width(self):
        """Retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """Set height
        Param Arg: value - value to be determined
        """
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height
        Param Arg: value - value to be determined
        """
        self.__height = value

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ set y
        Param arg: value - value to be determined"""
        self.__x = value

    @property
    def y(self):
        """Retrieves y """
        return self.__y

    @x.setter
    def y(self, value):
        """set y
        Param Arg: value - value to be determined"""
        self.__y = value
