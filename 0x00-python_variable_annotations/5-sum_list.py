#!/usr/bin/env python3
'''type-annotated funtion taking a list of floats and return sum'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return sum of list elements'''
    total: float = sum(input_list)
    return total
