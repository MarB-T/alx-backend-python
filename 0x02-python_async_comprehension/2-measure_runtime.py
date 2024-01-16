#!/usr/bin/env python3
'''Measure time of async comprehension function'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''function to measure runtime'''
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return end - start
