#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ returns a new matrix
    Param Arg1: matrix - must be a list of ints or floats
    Arg2: div - must a number can be int or float
    Raises Exceptions:
    TypeError - if each row in matrix not equal or if div is not a number
    ZeroDivisionError - if div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
           not all(isinstance(row, list) for row in matrix) or
           not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
