#!/usr/bin/env python3
"""reates a new task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a new task

    Args:
        max_delay (int): maximum delay time

    Returns:
        object: task object
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
