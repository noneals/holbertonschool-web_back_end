#!/usr/bin/env python3
"""Test script for measure_time only"""
measure_time = __import__('2-measure_runtime').measure_time

print("=== Testing measure_time separately ===")
avg_time = measure_time(3, 5)
print(f"measure_time(3, 5) returned: {avg_time}")
print(f"Type: {type(avg_time)}")
print("Test completed successfully!")