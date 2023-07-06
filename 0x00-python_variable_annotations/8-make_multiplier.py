#!/usr/bin/env python3
from typing import Callable
"""function that returns a function"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a funtion multiplier"""
    def mut(num: float) -> float:
        """returns result of multiplier * num"""
        return num * multiplier

    return mut
