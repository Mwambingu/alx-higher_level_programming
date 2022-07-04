#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """function to return class attr and mthds

    Args:
        obj (obj): the object with attrs and mthds
    """
    return dir(obj)
