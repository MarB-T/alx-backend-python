#!/usr/bin/env python3
''' async generator '''
import asyncio
import random


async def async_generator() -> float:
    '''ansynchronoi=us random generator'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
