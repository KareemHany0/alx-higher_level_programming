#!/usr/bin/python3
"""This class defines a square by: (based on 0-square.py)"""


class Square:
    """Exmaple of docstring.

    This class for represent the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Intialize square
        Args:
            size (int): size of square private instance attribute.
            position (int, int): Position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size (getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value to size (setter)"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

   @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)


    def my_print(self):
        """Print a square with '#' character"""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]

            for i in range(self.__size):
                [print(' ', end='') for j in range(self.__position[0])]
                [print('#', end='') for k in range(self.__size)]
                print()
