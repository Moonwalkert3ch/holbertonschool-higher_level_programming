#!/usr/bin/python3
"""
Defines a class square that inherits from rectangel
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class inheriting from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """initializes class square
        Param Arg1: size(int) - size of square
        Arg2: x(int) - coordinates
        Arg3: y(int) - coordinate
        Arg3: id(int) - identification
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Retrieves size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes
        Param Arg1: args - arg to assign to attr
        Arg2: kwargs - points to a dict key/value keyword argument
        """
        if args:
            for arg in args:
                if arg is args[0]:
                    self.id = arg
                elif arg is args[1]:
                    self.size = arg
                elif arg is args[2]:
                    self.x = arg
                elif arg is args[3]:
                    self.y = arg

        else:
            keywords = {"id", "size", "x", "y"}
            for key, value in kwargs.items():
                if key in keywords:
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary
