#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list1 in matrix:
        if not list1:
            return print("{}".format(""))
        for i in range(len(list1)):
            if i < len(list1) - 1:
                print("{:d}".format(list1[i]), end=" ")
            else:
                print("{:d}".format(list1[i]))
