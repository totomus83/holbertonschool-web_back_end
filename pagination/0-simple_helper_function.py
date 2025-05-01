#!/usr/bin/env python3
"""A simple helper function for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of (start_index, end_index) for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
