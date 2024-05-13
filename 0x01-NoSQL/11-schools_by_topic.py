#!/usr/bin/env python3
"""
This module contains a
 Python function that returns the list of
 school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function returns the list of schools
    with the specific topics needed
    """
    return mongo_collection.find({'topics': topic})
