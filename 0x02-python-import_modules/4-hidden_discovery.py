#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    store = dir(hidden_4)

    for i in store:
        if "__" not in i:
            print(i)
