#!/usr/bin/env python3
"""
type annotated function that return string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    string and int/float to tuple
    """
    return (k, float(v)**2)
