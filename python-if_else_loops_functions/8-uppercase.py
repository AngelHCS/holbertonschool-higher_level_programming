#!/usr/bin/python3
def uppercase(str):
    for idx in str:
        if ord('a') <= ord(idx) <= ord('z'):
            idx = chr(ord(idx) - 32)
        print("{}".format(idx), end="")
    print()
