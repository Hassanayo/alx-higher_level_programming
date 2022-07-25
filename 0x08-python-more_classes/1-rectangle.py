#!/usr/bin/python3
"""defining a rect"""

class Rectangle:
    """reps a rectangle"""

    def __init__(self, width=0, height=0):
        """init new rectangle
            
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
