"""
Given a cell with "it's a fib sequence" from slideshow,

    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def _check_window(x: int, y: int, z: int) -> int:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3 or data[1] == 0:
        return False
    for i in range(len(data) - 3):
        a, b, c = data[i], data[i + 1], data[i + 2]
        if not _check_window(a, b, c):
            return False
    return True
