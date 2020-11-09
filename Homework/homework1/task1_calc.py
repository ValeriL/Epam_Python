"""
The task is to find bugs for the function that check is the int a power of 2.

The case a = 0 was additionally processed.
"""


def check_power_of_2(a: int) -> bool:
    return bool(a and not (a & (a - 1)))
