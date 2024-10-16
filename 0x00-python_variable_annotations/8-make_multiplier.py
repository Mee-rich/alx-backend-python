#!/usr/bin/env pyhton3
"""
A type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) ->Callable[[float], float]:
    def multiplier_float(n: float) -> float:
        return n * multiplier

    return multiplier_float
