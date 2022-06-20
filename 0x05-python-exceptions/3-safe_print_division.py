#!/bin/usr/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("{} {}".format("Inside result:", result))
    return result
