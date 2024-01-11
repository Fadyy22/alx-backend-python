#!/usr/bin/env python3
"""
module containing make_multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return tuple of first str and square of second number"""
    return lambda x: (x * multiplier)
