#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list:
        return 0
    if x == 0:
        return 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print("{}".format(""))
        return i+1
    except IndexError:
        print("{}".format(""))
        return i
