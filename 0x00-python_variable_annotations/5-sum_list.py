#!/usr/bin/env python3
'''type-annotated funtion taking a list of floats and return sum'''


def sum_list(input_list: float) -> float:
    '''return sum of list elements'''
    total: float = 0
    for idx in range(len(input_list)):
        total += input_list[idx]
    return total
