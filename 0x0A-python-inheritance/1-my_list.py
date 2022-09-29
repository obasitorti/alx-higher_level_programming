#!/usr/bin/python3
"""Module defines a subclass MyList"""


class MyList(list):
    """prints a sorted list """

    def print_sorted(self):
        l = sorted(self)
        print(l)
