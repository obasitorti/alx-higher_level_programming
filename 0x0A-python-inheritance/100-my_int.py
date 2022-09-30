#!/usr/bin/python3
"""defines a class MyInt which is a subclass of int """


class MyInt(int):
    """class MyInt"""

    def __init__(self, value):
        """initialisation"""
        self.value = value

    def __eq__(self, value):
        """returns false for equality"""
        return (False)

    def __ne__(self, value):
        """returns true for inequality"""
        return (True)
