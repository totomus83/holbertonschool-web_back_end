#!/usr/bin/env python3
"""Simple pagination module."""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.
        """
        # 1. Validate input
        assert (
            isinstance(page, int) and page > 0
        ), "page must be a positive integer"

        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be a positive integer"

        # 2. Get start and end indexes using index_range
        start_index, end_index = index_range(page, page_size)

        # 3. Fetch data and return only the requested page
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []  # Out-of-range, return empty list

        return dataset[start_index:end_index]
