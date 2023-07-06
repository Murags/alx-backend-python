#!/usr/bin/env python3
from typing import Union
"""type annotation"""


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """returns a tuple"""
    return (k, v ** 2)
