#!/usr/bin/env python3
"""
module contains wait_n coroutine
"""

from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of delays"""
    delayes = []
    for i in range(n):
        delayes.append(await wait_random(max_delay))
    return sorted(delayes)
