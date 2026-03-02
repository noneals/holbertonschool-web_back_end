#!/usr/bin/env python3
"""0-simple_helper_function.py"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
