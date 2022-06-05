#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list1 in matrix:
        for i in list1:
            print("{:d}".format(i), end=" ")
        print("{}".format(""))
