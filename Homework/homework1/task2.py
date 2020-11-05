"""
Given a cell with "it's a fib sequence" from slideshow.

Please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def _check_window(x: int, y: int, z: int) -> int:
    return (x + y) == z


def _check_fibonacci(data: Sequence[int]) -> bool:
    """
    Check the rule of fib seq D[i] + D[i+1] = D[i+2].

    Created for improve Cognitive Complexity.
    """
    for i in range(len(data) - 2):
        a, b, c = data[i], data[i + 1], data[i + 2]
        if not _check_window(a, b, c):
            return False
    return True


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    if data[0] != 0 and data[1] != 1:
        return False
    elif data[0] != 1 and data[1] != 1:
        return False
    return _check_fibonacci(data)
