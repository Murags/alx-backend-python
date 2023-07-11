#!/usr/bin/env python3
"""module exploring generator functions"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yeilds random float after every one second

    Yields:
        Generator[float]: random float
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
