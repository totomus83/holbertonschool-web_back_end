#!/usr/bin/env python3
"""
type annotated function that return the sum of a list of int
as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of list of integers"""
    return sum(mxd_lst)
