#!/usr/bin/python3
n_rev = 0


def mirror(num):
    global n_rev
    if num > 0:
        rem = num % 10
        n_rev = (n_rev * 10) + rem
        mirror(num // 10)
    return n_rev


for i in range(0, 100):
    if i < 10 and i > 0:
        print("{:02d}".format(i), end=", ")
    elif i == 89:
        print("{}".format(89))
    else:
        n_rev = 0
        i_rev = mirror(i)
        if i < i_rev:
            print("{}".format(i), end=", ")
