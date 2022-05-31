#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range(0, 10):
        if number is 8 and number2 is 9:
            print("{:d}{:d}".format(number, number2))
        elif num < number2:
            print("{:d}{:d}".format(number, number2), end=", ")
