#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    prev_value = 0
    total = 0

    for char in reversed(roman_string):
        if char in roman_to_int_map:
            int_value = roman_to_int_map[char]
            if int_value < prev_value:
                total -= int_value
            else:
                total += int_value
            prev_value = int_value
        else:
            return 0  # Return 0 if an invalid character is found

    return total
