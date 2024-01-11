#!/usr/bin/env python3
"""
module containing element_length function
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return length of a list of sequence"""
    return [(i, len(i)) for i in lst]
