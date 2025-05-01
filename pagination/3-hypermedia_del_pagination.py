#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing:
        - index: the starting index of the current page
        - next_index: the next index to query
        - page_size: the size of the current page
        - data: the actual dataset page
        """

        # Validate index
        assert (
            isinstance(index, int) and index >= 0
        ), "index must be a non-negative integer"

        # Dataset and indexed dataset
        dataset = self.dataset()
        indexed_dataset = self.indexed_dataset()

        # Prepare the current page of data
        data = []
        current_index = index
        for i in range(page_size):
            # Skip deleted items by checking if the current index
            # exists in the indexed dataset
            while current_index not in indexed_dataset:
                current_index += 1
            # Append the valid item to data
            data.append(indexed_dataset[current_index])
            current_index += 1

        # Next index should be the first index
        # after the last item in the current page
        next_index = current_index if current_index < len(dataset) else None

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
