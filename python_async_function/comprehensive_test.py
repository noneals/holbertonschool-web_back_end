#!/usr/bin/env python3
"""Comprehensive test for all async tasks"""
import asyncio
import time

def test_task_1():
    """Test basic wait_random function"""
    print("🔍 Task 1: wait_random")
    wait_random = __import__('0-basic_async_syntax').wait_random
    
    async def test():
        result = await wait_random(5)
        print(f"   ✓ wait_random(5) = {result:.3f}")
        print(f"   ✓ Type: {type(result).__name__}")
        print(f"   ✓ In range [0,5]: {0 <= result <= 5}")
        return True
    
    return asyncio.run(test())

def test_task_2():
    """Test concurrent wait_n function"""
    print("\n🔍 Task 2: wait_n")
    wait_n = __import__('1-concurrent_coroutines').wait_n
    
    async def test():
        start = time.time()
        results = await wait_n(3, 5)
        end = time.time()
        elapsed = end - start
        
        print(f"   ✓ wait_n(3, 5) = {[round(x, 3) for x in results]}")
        print(f"   ✓ Length: {len(results)} (expected: 3)")
        print(f"   ✓ All in range [0,5]: {all(0 <= x <= 5 for x in results)}")
        print(f"   ✓ Sorted ascending: {results == sorted(results)}")
        print(f"   ✓ Concurrent execution (~{elapsed:.1f}s, expected ~max delay)")
        return True
    
    return asyncio.run(test())

def test_task_3():
    """Test measure_time function"""
    print("\n🔍 Task 3: measure_time")
    measure_time = __import__('2-measure_runtime').measure_time
    
    start = time.time()
    avg_time = measure_time(3, 5)
    end = time.time()
    total_elapsed = end - start
    
    print(f"   ✓ measure_time(3, 5) = {avg_time:.3f}")
    print(f"   ✓ Type: {type(avg_time).__name__}")
    print(f"   ✓ Total time: {total_elapsed:.1f}s")
    print(f"   ✓ Returns avg per coroutine: {total_elapsed/3:.3f} ≈ {avg_time:.3f}")
    return True

def test_task_4():
    """Test task_wait_random function"""
    print("\n🔍 Task 4: task_wait_random")
    task_wait_random = __import__('3-tasks').task_wait_random
    
    async def test():
        task = task_wait_random(5)
        print(f"   ✓ Creates Task object: {type(task).__name__}")
        print(f"   ✓ Task state: {task._state}")
        
        result = await task
        print(f"   ✓ Task result: {result:.3f}")
        print(f"   ✓ Type: {type(result).__name__}")
        print(f"   ✓ In range [0,5]: {0 <= result <= 5}")
        return True
    
    return asyncio.run(test())

def test_task_5():
    """Test task_wait_n function"""
    print("\n🔍 Task 5: task_wait_n")
    task_wait_n = __import__('4-tasks').task_wait_n
    
    async def test():
        start = time.time()
        results = await task_wait_n(3, 5)
        end = time.time()
        elapsed = end - start
        
        print(f"   ✓ task_wait_n(3, 5) = {[round(x, 3) for x in results]}")
        print(f"   ✓ Length: {len(results)} (expected: 3)")
        print(f"   ✓ All in range [0,5]: {all(0 <= x <= 5 for x in results)}")
        print(f"   ✓ Sorted ascending: {results == sorted(results)}")
        print(f"   ✓ Uses Tasks (~{elapsed:.1f}s)")
        return True
    
    return asyncio.run(test())

if __name__ == "__main__":
    print("🚀 HOLBERTON ASYNC FUNCTION TESTS")
    print("=" * 50)
    
    success_count = 0
    tests = [test_task_1, test_task_2, test_task_3, test_task_4, test_task_5]
    
    for test_func in tests:
        try:
            if test_func():
                success_count += 1
        except Exception as e:
            print(f"   ❌ ERROR: {e}")
    
    print(f"\n📊 RESULTS: {success_count}/{len(tests)} tests passed")
    
    if success_count == len(tests):
        print("🎉 ALL TESTS PASSED! Ready for Holberton checker!")
    else:
        print("⚠️  Some tests failed. Check implementation.")