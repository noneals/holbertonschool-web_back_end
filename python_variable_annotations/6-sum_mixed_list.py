#!/usr/bin/env python3
"""Module for summing a list of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all elements in a list of integers and floats

    Args:
        mxd_lst: List of integers and floats

    Returns:
        Sum of all numbers as a float
    """
    return sum(mxd_lst)
