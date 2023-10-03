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
