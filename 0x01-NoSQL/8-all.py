#!/usr/bin/env python3
"""Import required modules"""
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List[dict]:
    """Lists all documents in a MongoDB collection."""
    documents = list(mongo_collection.find())

    if not documents:
        return []

    return documents
