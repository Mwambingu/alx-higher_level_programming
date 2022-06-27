#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds 2 integers and returns the result
    Args:
        a (int): the first integer
        b (int): the second integer
    Return: result of addition
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
