#!/usr/bin/python3
def print_last_digit(number):
    last = int(repr(number)[-1])
    if (number > 0):
        return last
    elif (number == 0):
        return last
    else:
        return last * -1
