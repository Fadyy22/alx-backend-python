#!/usr/bin/env python3
"""
module containing sum_mixed_list function
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of all numbers in a list"""
    return sum(mxd_lst)
