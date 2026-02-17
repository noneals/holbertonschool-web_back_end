#!/usr/bin/env python3
"""Test script for async functions"""
import asyncio
import time

# Import the modules
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n
measure_time = __import__('2-measure_runtime').measure_time
task_wait_random = __import__('3-tasks').task_wait_random
task_wait_n = __import__('4-tasks').task_wait_n


async def test_all():
    print("=== Testing Task 1: wait_random ===")
    result = await wait_random(5)
    print(f"wait_random(5) returned: {result}")
    print(f"Type: {type(result)}, In range [0,5]: {0 <= result <= 5}")
    
    print("\n=== Testing Task 2: wait_n ===")
    results = await wait_n(3, 5)
    print(f"wait_n(3, 5) returned: {results}")
    print(f"Length: {len(results)}, All in range: {all(0 <= x <= 5 for x in results)}")
    print(f"Sorted: {results == sorted(results)}")
    
    print("\n=== Testing Task 3: measure_time ===")
    avg_time = measure_time(3, 5)
    print(f"measure_time(3, 5) returned: {avg_time}")
    print(f"Type: {type(avg_time)}")
    
    print("\n=== Testing Task 4: task_wait_random ===")
    try:
        task = task_wait_random(5)
        print(f"task_wait_random(5) returned: {task}")
        print(f"Type: {type(task)}")
        result = await task
        print(f"Task result: {result}")
    except Exception as e:
        print(f"Error in task_wait_random: {e}")
    
    print("\n=== Testing Task 5: task_wait_n ===")
    try:
        results = await task_wait_n(3, 5)
        print(f"task_wait_n(3, 5) returned: {results}")
        print(f"Length: {len(results)}, All in range: {all(0 <= x <= 5 for x in results)}")
        print(f"Sorted: {results == sorted(results)}")
    except Exception as e:
        print(f"Error in task_wait_n: {e}")


if __name__ == "__main__":
    asyncio.run(test_all())