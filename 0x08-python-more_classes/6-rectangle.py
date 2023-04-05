#!/usr/bin/python3
# Author: Erick Karanja
'''defining class Rectangle.'''


class Rectangle:
    '''Represent class rectangle
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''initializes objects to class rectangle'''
        type(self).number_of_instances += 1
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
        value(int): The value of width.
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
        value(int): The value of width.
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

    def __str__(self):
        '''Returns the printable representation of a rectangle
        Represents rectangle with # characters.
        '''
        if self._width == 0 or self._height == 0:
            return ("")

        rect = []
        for i in range(self._height):
            [rect.append('#') for j in range(self._width)]
            if i != self._height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):
        '''returns the string representation of a rectangle'''
        rect = "Rectangle(" + str(self._width)
        rect += ", " + str(self._height) + ")"
        return (rect)

    def __del__(self):
        '''prints message for every deletion of Rectangle'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
