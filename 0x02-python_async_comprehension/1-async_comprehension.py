#!/usr/bin/env python3
"""asynchronous list comprehension"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """list comprehension with async

    Returns:
        List[float]: list of random numbers generated
    """
    return [i async for i in async_generator()]
