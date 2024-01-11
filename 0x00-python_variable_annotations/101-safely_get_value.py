#!/usr/bin/env python3
"""
module containing safely_get_value function
"""


from typing import Any, Mapping, Union, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default=None) -> Union[T, None]:
    """gets the value of a key in dct if the key exists"""
    if key in dct:
        return dct[key]
    else:
        return default
