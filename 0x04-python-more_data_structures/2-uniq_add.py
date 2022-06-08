#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_to_use = set()
    result = 0
    set_to_use.update(my_list)
    for i in set_to_use:
        result += i
    return result
