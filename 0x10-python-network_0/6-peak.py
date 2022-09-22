#!/usr/bin/python3
"""
Contains a functon that finds the peak of a list
"""


def find_peak(list_of_integers):
    """Function to find the peak of a list"""
    large = 0
    if not list_of_integers:
        return None
    
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if len(list_of_integers) == 2:
        return max(list_of_integers)

    for i in list_of_integers:
        if i > large:
            large = i
    return large
