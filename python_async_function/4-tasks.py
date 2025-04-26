#!/usr/bin/env python3
import asyncio
from typing import List

"""
Take the code from wait_n and alter it into a new function task_wait_n
"""

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n func
    """
    delays = []
    coroutines = []
    for number_coroutines in range(n):
        coroutines.append(task_wait_random(max_delay))

    for coroutine in asyncio.as_completed(coroutines):
        # as_completed order coroutines by end of excecution (fastest first)
        delay = await coroutine
        delays.append(delay)

    return delays
