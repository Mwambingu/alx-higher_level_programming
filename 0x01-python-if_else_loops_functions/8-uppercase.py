#!/usr/bin/python3i

def uppercase(str):
    str2 = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            str2 += chr((ord(i) - 32))
        else:
            str2 += i
    print("{}".format(str2))
