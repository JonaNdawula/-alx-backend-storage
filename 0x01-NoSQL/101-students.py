#!/usr/bin/env python3
"""
This module contains a
python function that returns
students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    best_student = mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': '$topic.score'}
            }
        },
        {'$sort': {'averageScore': -1}}
    ])

    return best_student
