#!/usr/bin/env python3
"""
Module for async generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator that yields random numbers

    Yields:
        Random float between 0 and 10, after waiting 1 second each time
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
