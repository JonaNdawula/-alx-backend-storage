#!/usr/bin/env python3

"""
 This module lista all the
 documents in a collection
"""


def list_all(mongo_collection):
    """
    Return an empty list if no
    document in the collection
    """
    return list(mongo_collection.find())
