#!/usr/bin/env python3
"""type annotation of iterables"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return the lenght of iterables'''
    return [(i, len(i)) for i in lst]
