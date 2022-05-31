#!/usr/bin/python3
def remove_char_at(str1, n):
    str2 = ""
    for i in range(0, len(str1)):
        if i != n:
            str2 += str1[i]
    return str2
