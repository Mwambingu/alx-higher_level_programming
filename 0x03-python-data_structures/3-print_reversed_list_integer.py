#!/usr/bin/python3
count = 0
def print_reversed_list_integer(my_list=[]):
    count = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[count]))
        count -= 1
