#!/usr/bin/python3
"""defines a func"""
import json


def from_json_string(my_str):
    """returns the python object rep of a json string="""
    return json.loads(my_str)