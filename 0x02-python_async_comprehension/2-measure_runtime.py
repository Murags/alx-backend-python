#!/usr/bin/env python3
"""Running coroutines concurrently"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Runs concurrent coroutines

    Returns:
        float: average time taken
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()

    return end_time - start_time
