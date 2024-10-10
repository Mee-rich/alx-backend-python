#!/usr/bin/env python3
"""
Use mypy to validate the folowing piece of code
and apply any necessary changes.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
            item for item in lst
            for _ in range(factor)
            ]
    return zoomed_in

array = [12, 72, 91]

zoomed_2x = zoom_array(array)

zoomed_3x = zoom_array(array, 3)
