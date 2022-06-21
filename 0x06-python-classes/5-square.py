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

    def my_print(self):
        """Prints a square using #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print("{}".format(""))

    @property
    def size(self):
        """Getter method to return value of size

        Setter reassigns the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
