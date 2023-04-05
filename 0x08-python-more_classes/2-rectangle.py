#!/usr/bin/python3
# Author: Erick Karanja
'''Defining class Rectangle'''


class Rectangle:
    '''initializes class rectangle'''
    def __init__(self, width=0, height=0):
        '''initializes objects to class rectangle
        args:
        width (int):width of the rectangle.
        height (int):height of the rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets/sets the width value of a rectangle'''
        return (self._width)

    @width.setter
    def width(self, value):
        '''sets the width value of a rectangle
        args:
        value (int): The value of width.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        '''gets/sets the height value of a rectangle'''
        return (self._height)

    @height.setter
    def height(self, value):
        '''sets the width value of a rectangle
        args:
        value (int): The value of width.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def perimeter(self):
        '''finds the perimeter of a rectangle'''
        if self._height == 0 or self._width == 0:
            return (0)
        else:
            return ((self.height * 2) + (self.width * 2))

    def area(self):
        '''finds area of a rectangle'''
        return (self._height * self._width)
