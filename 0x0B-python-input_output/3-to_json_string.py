#!/usr/bin/python3
"""defines a function"""
import json


def to_json_string(my_obj):
    """returns the json representation of a string object"""
    return json.dumps(my_obj)