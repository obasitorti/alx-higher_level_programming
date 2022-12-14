#!/usr/bin/python3
"""
    project to define a class square
"""


class Square:
    """
        defines the class of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
            initialization of the square
            position is for the coordinates and
            size is for the size
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
            returns the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            determines the conditiones
            for the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
            returns the co-ordinates of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
            determines the conditions for the co-ordinates 
            of the square
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1])
                is not int or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
            returns the area of the square
        """
        return (self.__size ** 2)

    def pos_print(self):
        """
            returns the position in spaces
        """
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.__position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.__position[0]):
                pos += " "
            for j in range(self.__size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
