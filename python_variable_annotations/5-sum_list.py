#!/usr/bin/env python3

"""
type annotated function that return sum of a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum"""
    return sum(input_list)
