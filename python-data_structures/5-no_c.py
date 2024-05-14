#!/usr/bin/python3
def no_c(org_string):
    string_noc =("")
    for char in org_string:
        if char != 'c' and char != 'C':
            string_noc += char
    return string_noc
