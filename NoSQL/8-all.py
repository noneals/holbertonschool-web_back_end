#!/usr/bin/env python3
""" 8-all """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents in a collection """
    documents = mongo_collection.find()
    return documents
