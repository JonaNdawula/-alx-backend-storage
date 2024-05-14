#!/usr/bin/env python3

"""
Script using pymongo
to get required statistics
"""

from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client['logs']

collection = db['nginx']

total_logs = collection.count_documents({})

methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
method_count = [collection.count_documents({'method': method})
                for method in methods]

status_get_count = collection.count_documents({'methods': 'GET',
                                              'path': '/status'})

print(f'{total_logs} logs')
print('Methods:')
for method, count in zip(methods, method_count):
    print(f'\t{method}: {count}')
print(f'GET /status: {status_get_count}')
