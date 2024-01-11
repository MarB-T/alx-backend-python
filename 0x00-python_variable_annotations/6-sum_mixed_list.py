#!/usr/bin/env python3
''' type annotation of mixed list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''process list containing integers and floats'''
    return sum(mxd_lst)
