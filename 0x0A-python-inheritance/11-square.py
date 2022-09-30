#!/usr/bin/python3
"""module defines a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class defines a square
        which is a subclass of Rectangle
    """

    def __init__(self, size):
        """initialisation"""
        super().integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """returns the area"""
        return self.__size ** 2
