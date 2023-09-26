#!/usr/bin/python3
""" Defines a function that prints the list, but sorted (ascending sort) """


class MyList(list):
    """class that inherits the list """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort) """
        print(sorted(self))
