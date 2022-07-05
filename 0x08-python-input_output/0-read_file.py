#!/usr/bin/python3
"""
Contains a function that reads & returns a files contents
"""


def read_file(filename=""):
    """Function that reads a file and returns the contents
    read.

    Args:
        filename (str): the string that contains the filename

    Return: content of file
    """
    with open(filename, encoding="utf8") as f:
        return f.read()
