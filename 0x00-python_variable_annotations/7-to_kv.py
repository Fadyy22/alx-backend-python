#!/usr/bin/env python3
"""
module containing to_kv function
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of first str and square of second number"""
    return (k, float(v**2))
