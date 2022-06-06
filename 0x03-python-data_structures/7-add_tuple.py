#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        if not tuple_b:
            tuple_c = (0, 0)
            return tuple_c
    if len(tuple_a) == 1 and len(tuple_b) == 1:
        v_a0 = tuple_a[0]
        v_a1 = 0
        v_b0 = tuple_b[0]
        v_b1 = 0
    elif len(tuple_a) == 1:
        v_a0 = tuple_a[0]
        v_a1 = 0
        v_b0 = tuple_b[0]
        v_b1 = tuple_b[1]
    elif len(tuple_b) == 1:
        v_a0 = tuple_a[0]
        v_a1 = tuple_a[1]
        v_b0 = tuple_b[0]
        v_b1 = 0
    elif not tuple_a:
        v_a0 = 0
        v_a1 = 0
        v_b0 = tuple_b[0]
        v_b1 = tuple_b[1]
    elif not tuple_b:
        v_a0 = tuple_a[0]
        v_a1 = tuple_a[1]
        v_b0 = 0
        v_b1 = 0
    else:
        v_a0 = tuple_a[0]
        v_a1 = tuple_a[1]
        v_b0 = tuple_b[0]
        v_b1 = tuple_b[1]
    val_1 = v_a0 + v_b0
    val_2 = v_a1 + v_b1
    tuple_c = (val_1, val_2)
    return tuple_c
