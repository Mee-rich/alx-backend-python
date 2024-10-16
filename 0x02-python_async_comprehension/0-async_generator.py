#!/usr/bin/env python3

import asyncio
import random
from typing import Generator

""" Coroutine that loops 10 times, asynchronously waits 1 secondthen yields a random number between 0 and 10.
"""


async def async_generator() -> Generator[float, None, None]:

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
