#!/usr/bin/env python3
'''type annotation Any'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''using Any annotation'''
    if lst:
        return lst[0]
    else:
        return None
