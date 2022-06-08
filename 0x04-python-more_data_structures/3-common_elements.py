#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_c = set()
    set_c = {item for item in set_1 if item in set_2}
    return set_c
