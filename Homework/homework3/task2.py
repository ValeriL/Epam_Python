"""
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.

Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Do some weird voodoo magic calculations."""
    time.sleep(random.randint(1, 3))  # noqa
    data = hashlib.md5(str(value).encode()).digest()  # noqa
    return sum(struct.unpack("<" + "B" * len(data), data))


def speed_up_calculate() -> float:
    with Pool(30) as pool:
        start = time.time()
        pool.map(slow_calculate, range(0, 500))
        return time.time() - start
