#!/usr/bin/env python3
""" using type annotation to return a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function to return a callable function'''
    def mult(m: float) -> float:
        '''multiply multiplier by m'''
        return m * multiplier
    return mult
