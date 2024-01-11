#!/usr/bin/env python3
"""
module containing element_length function
"""

from typing import Iterable, List, Tuple


def element_length(lst: Iterable) -> List[Tuple[Iterable, int]]:
    """return length of a list of sequence"""
    return [(i, len(i)) for i in lst]
