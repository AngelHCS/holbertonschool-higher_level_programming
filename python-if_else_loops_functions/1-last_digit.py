#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10 * (-1 if number < 0 else 1) #hacky fix for negatives
if last_digit > 5:
    message = "and is greater than 5"

elif last_digit == 0:
    message = "and is 0"

else:
    message = "and is less than 6 and not 0"

print("Last digit of", number, "is", last_digit, message)
