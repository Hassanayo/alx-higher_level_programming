#!/usr/bin/python3
def no_c(my_string):
    cs = ["c", "C"]
    new_word = "".join([i for i in my_string if i not in cs])
    return new_word
