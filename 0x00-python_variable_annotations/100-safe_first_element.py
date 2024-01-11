#!/usr/bin/env python3
"""
module containing safe_first_element function
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """gets the first element of a sequence if it exists"""
    if lst:
        return lst[0]
    else:
        return None
