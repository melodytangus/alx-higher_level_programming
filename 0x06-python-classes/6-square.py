#!/usr/bin/python3
'''Initialize Class Square
'''

class Square:
    '''Initialize Class Square
    '''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if type(position) != tuple and len(position) != 2 and position[0] < 0 and position [1] <0 :
            raise TypeError("position must be a tuple of 2 positive integers") 
        self.__position = value

    def area(self):
        return (self.size * self.size)
    def my_print(self):
         if self.__size == 0:
             print("") 
             return
         [print("") for i in range(0, self.__position[1])]
          for i in range(0, self.__size):
              [print(" ", end="") for j in range(0, self.__position[0])]
              [print("#", end="") for k in range(0, self.__size)]
              print ("") 
