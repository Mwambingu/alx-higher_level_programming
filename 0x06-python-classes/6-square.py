#!/usr/bin/python3
""" Module with a class Square """


class Square:
    """A class that defines a square.


    Attributes:
        __size (int): size of the square's side
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.
        Args:
            size (int): size of the square's side
            position (tuple): tuple containing pos of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        if type(position) is tuple and len(position) == 2:
            if type(position[0]) is int and type(position[1]) is int:
                self.__position = position
            else:
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                        )

    def area(self):
        """ Calculates the area of the square.
            Return: result of the calculation
        """
        result = self.__size ** 2
        return result

    def my_print(self):
        """prints the square

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for x in range(self.__size)]))

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

    @property
    def position(self):
        """Getter method to return value of position

        Setter reassigns the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) is tuple and len(position) == 2:
            if type(position[0]) is int and type(position[1]) is int:
                self.__position = value
            else:
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                        )
