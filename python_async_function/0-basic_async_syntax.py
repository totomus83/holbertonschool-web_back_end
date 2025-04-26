#!/usr/bin/env python3
"""
random delay from 0 to max delay and return a float
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
