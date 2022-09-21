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
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
            

    def area(self):
        """
            returns the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
          prints the square using #s  
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
