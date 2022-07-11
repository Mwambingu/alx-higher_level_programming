#!/usr/bin/python3
"""
Contains a class base
"""

class Base:
    """Base Class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

