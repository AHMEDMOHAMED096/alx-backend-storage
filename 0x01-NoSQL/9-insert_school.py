#!/usr/bin/env python3
"""A Python function that inserts a new document"""


def insert_school(mongo_collection, **kwargs):
    """A Python function that inserts a new document
    in a collection based on kwargs"""
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
