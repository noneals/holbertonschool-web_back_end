#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
	"""Return the list of school having a specific topic"""
	result = mongo_collection.find({"topics": topic})
	return list(result)
