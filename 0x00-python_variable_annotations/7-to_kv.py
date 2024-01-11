#!/usr/bin/env python3
'''Type annotation where an argument can be either of two types'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return a tuple of arguments passed'''
    return (k, float(v * v))
