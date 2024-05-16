#!/usr/bin/python3
def raise_exception_msg(message="C is fun"):  # we are not using C but ok
    if [message] != 50:
        raise ValueError("invalid value")
    else:
        print(message)
