#!/usr/bin/env python3
"""
module contains wait_random coroutine
"""

import asyncio
import random


async def wait_random(make_delay: int = 10) -> float:
    """function that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it"""
    value = random.uniform(0, make_delay)
    await asyncio.sleep(value)
    return value
