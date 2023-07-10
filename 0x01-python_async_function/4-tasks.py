#!/usr/bin/env python3
"""returns list of time delays"""
import asyncio
wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """returns list of time delays by the wait_random

    Args:
        n (int): number of times to delay
        max_delay (int): maximum seconds to delay

    Returns:
        list: list of floats with are seconds delayed
    """
    time_list = []

    for i in range(n):
        time = await wait_random(max_delay)
        time_list.append(time)

    return sorted(time_list)
