#!/usr/bin/env python3
"""type annotation"""
from typing import Union


def to_kv(k: str, v: Union[float, int]) -> tuple:
    """returns a tuple"""
    return (k, v ** 2)
