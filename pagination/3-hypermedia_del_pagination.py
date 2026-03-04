#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Any, Dict, List, Optional


class Server:
    """Paginate a dataset of popular baby names with deletion resilience."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading it from CSV on first access."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by original row position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: Optional[int] = None,
        page_size: int = 10
    ) -> Dict[str, Any]:
        """Return a deletion-resilient page starting from the provided index."""
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        max_index = max(dataset.keys()) if dataset else -1
        assert index <= max_index

        data = []
        current_index = index

        while len(data) < page_size and current_index <= max_index:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
