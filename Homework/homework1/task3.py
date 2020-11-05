"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.

Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
import io
from typing import Tuple


def _find_maximum_and_minimum(file: io.StringIO()) -> Tuple[int, int]:
    """Find the max and min values in the file."""
    min_val = int(file.readline())
    max_val = min_val
    for line in file:
        new_val = int(line)
        min_val = min(min_val, new_val)
        max_val = max(max_val, new_val)
    file.close()
    return min_val, max_val


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    file = open(file_name, "r")
    return _find_maximum_and_minimum(file)
