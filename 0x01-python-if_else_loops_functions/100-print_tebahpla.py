#!/usr/bin/python3
mv_back = 122
while mv_back > 96:
    if mv_back % 2 != 0:
        upperC = chr(mv_back - 32)
        print("{}".format(upperC), end="")
    else:
        print("{}".format(chr(mv_back)), end="")
    mv_back -= 1
