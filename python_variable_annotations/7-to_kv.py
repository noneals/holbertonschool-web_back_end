#!/usr/bin/env python3
"""Module for creating a tuple from string and squared number"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with string and squared value

    Args:
        k: String key
        v: Integer or float value

    Returns:
        Tuple of string and squared value as float
    """
    return (k, v ** 2)
