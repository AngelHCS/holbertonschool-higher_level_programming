#!/usr/bin/python3
def raise_exception_msg(message="C is fun"):  # we are not using C but ok
    try:
        raise_expection_msg("C is fun")
    except NameError:
        print("Name error")
        print(message)
