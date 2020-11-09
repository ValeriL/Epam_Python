from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    Given an array of size n, find the most common and the least common elements.

    The most common element is the element that appears more than n // 2 times.
    The least common element is the element that appears fewer than other.
    You may assume that the array is non-empty and the most common element
    always exist in the array.

    If there are more than one minor, the function returns the min value
    """
    count_el = defaultdict(int)
    for el in inp:
        count_el[el] += 1
    max_val = max(count_el, key=count_el.get)
    min_val = min(count_el, key=count_el.get)
    return max_val, min_val
