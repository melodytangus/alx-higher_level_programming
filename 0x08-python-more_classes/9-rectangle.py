#!/usr/bin/python3
# Author: Erick Karanja
'''Defining class rectangle.'''


class Rectangle:
    '''Represent class rectangle
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    '''

    number_of_instances = 0
    print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns rectangle with the biggest area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Raises:
            TypeError: if either rect_1 or rect_2 is not a rectangle.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        '''Returns new rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the two rectangles.
        '''
        return (cls(size, size))

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
