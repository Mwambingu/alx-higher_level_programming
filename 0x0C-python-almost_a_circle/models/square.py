#!/usr/bin/python3
"""
Contains square class
"""
from rectangle import Rectangle

class Square(Rectangle):
    """The square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes an object Square
        Args:
            size (int): size of the Square
            x (int): contains the x axis of the Square
            y (int): contains the y axis of the Square
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
