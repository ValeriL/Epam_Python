"""
Classic task, a kind of walnut for you.

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import defaultdict
from typing import List, Mapping


def add_to_dict(x: List[int], y: List[int]) -> Mapping[int, int]:
    """Add amount of elements repeats' into the dict[num, amount of repeats]."""
    xy_dict = defaultdict(int)
    for el_1 in x:
        for el_2 in y:
            xy_dict[el_1 + el_2] += 1
    return xy_dict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Check sum of four elements from four lists.

    And count an amount of sums equal to zero.
    """
    count = 0
    ab_dict = add_to_dict(a, b)
    cd_dict = add_to_dict(c, d)

    for key in ab_dict:
        key_neg = (-1) * key
        if key_neg in cd_dict:
            count += ab_dict[key] * cd_dict[key_neg]
    return count
