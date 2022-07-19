#!/usr/bin/python3
"""class square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """Square
        Args:
            size(int): size of the square
        """

        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """area"""
    def area(self):
        """Square
        Returns:
            returns the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
        if self.__size == 0:
            print("")
