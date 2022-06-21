#!/usr/bin/python3
""" Module with a class Square """


class Square:
    """A class that defines a square.


    Attributes:
        __size (int): size of the square's side
    """
    def __init__(self, size):
        """Initializes the square.
        Args:
            size (int): size of the square's side
        """
        self.__size = size
