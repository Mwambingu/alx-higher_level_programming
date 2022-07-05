#!/usr/bin/python3
"""
Contains a function that reads & prints a files contents
"""


def read_file(filename=""):
    """Function that reads a file and prints the contents
    read.

    Args:
        filename (str): the string that contains the filename
    """
    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")
