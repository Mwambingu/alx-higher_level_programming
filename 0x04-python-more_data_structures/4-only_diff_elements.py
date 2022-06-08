#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_a, set_b, set_c = set(), set(), set()

    set_a = {item for item in set_1 if item not in set_2}
    set_b = {item for item in set_2 if item not in set_1}

    set_c.update(set_a, set_b)
    return set_c
