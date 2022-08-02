#!/usr/bin/python3
"""defining a function"""

def append_write(filename="", text=""):
    """ appends a srting
    Args: 
        filename(str): The name of the file
        text(str): The text to append
    Returns: 
            The new appended file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)