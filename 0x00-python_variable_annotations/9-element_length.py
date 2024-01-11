#!/usr/bin/env python3
"""type annotation of iterables"""
from typing import Iterable, Tuple, List


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''return the lenght of iterables'''
    return [(i, len(i)) for i in lst]
