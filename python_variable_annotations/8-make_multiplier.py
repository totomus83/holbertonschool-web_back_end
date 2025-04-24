#!/usr/bin/env python3
"""
type-annotated function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""

    def multiply_function(number: float) -> float:
        return number * multiplier
    return multiply_function
