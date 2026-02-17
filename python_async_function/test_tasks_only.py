#!/usr/bin/env python3
"""Test script for task functions"""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random
task_wait_n = __import__('4-tasks').task_wait_n

async def test_tasks():
    print("=== Testing task_wait_random ===")
    try:
        # Create task
        task = task_wait_random(5)
        print(f"task_wait_random(5) returned: {task}")
        print(f"Type: {type(task)}")
        # Await the task
        result = await task
        print(f"Task result: {result}")
        print(f"Result type: {type(result)}, In range [0,5]: {0 <= result <= 5}")
    except Exception as e:
        print(f"Error in task_wait_random: {e}")
    
    print("\n=== Testing task_wait_n ===")
    try:
        results = await task_wait_n(3, 5)
        print(f"task_wait_n(3, 5) returned: {results}")
        print(f"Length: {len(results)}, All in range: {all(0 <= x <= 5 for x in results)}")
        print(f"Sorted: {results == sorted(results)}")
    except Exception as e:
        print(f"Error in task_wait_n: {e}")

if __name__ == "__main__":
    asyncio.run(test_tasks())