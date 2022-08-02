#!/usr/bin/python3
"""defines a function"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:
    Args:
        filename (string): the name of the file with the data
    Returns:
        object: the python object created
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f) 