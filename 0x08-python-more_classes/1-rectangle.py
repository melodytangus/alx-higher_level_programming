#!/usr/bin/python3
# Author: Erick Karanja
'''Defining a Rectangle class.'''


class Rectangle:
    '''initializing class rectangle'''

    def __init__(self, width=0, height=0):
        '''initializes class rectangle.

        args:
            width (int):width odf the rectangle.
            height (int):height of the rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''defining the width of the rectangle'''
        return self._width

    @width.setter
    def width(self, value):
        '''sets the width value'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        '''defining the height of the rectangle'''
        return self._height

    @height.setter
    def height(self, value):
        '''sets the height value
        args:
            value(int):height of the rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
