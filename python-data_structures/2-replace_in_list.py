#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):  # i should use and more often
        my_list[idx] = element
        return my_list
