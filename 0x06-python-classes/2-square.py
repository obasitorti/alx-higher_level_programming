#!/usr/bin/python3
"""
    module to define a squuare class
"""


class Square:
    """
        definition of class square
    """

    def __init__(self, size=0):
        """
            arguments are self and size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
