#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(c) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
