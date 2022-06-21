#!/usr/bin/python3
""" Module with a class Square """


class Square:
    """A class that defines a square.


    Attributes:
        __size (int): size of the square's side
    """
    def __init__(self, size=0):
        """Initializes the square.
        Args:
            size (int): size of the square's side
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """ Calculates the area of the square.
            Return: result of the calculation
        """
        result = self.__size ** 2
        return result
