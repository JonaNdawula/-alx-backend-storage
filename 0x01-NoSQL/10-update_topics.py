#!/usr/bin/env python3
"""
This module contains
a Python function that changes all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    This function changes
    all topics of a school
    document based on name
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
