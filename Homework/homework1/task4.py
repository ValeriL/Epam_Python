"""
Classic task, a kind of walnut for you.

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List, Mapping


def create_dict(x: int, x_dict: Mapping[int, int]) -> Mapping[int, int]:
    """Add repeated elements into the dictionary."""
    if x in x_dict:
        x_dict[x] += 1
    else:
        x_dict[x] = 1
    return x_dict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Find amount of sums equal to zero."""
    count = 0
    ab_dict, cd_dict = {}, {}
    n = len(a)
    for i in range(n):
        for j in range(n):
            ab = a[i] + b[j]
            ab_dict = create_dict(ab, ab_dict)
            cd = c[i] + d[j]
            cd_dict = create_dict(cd, cd_dict)

    for key in ab_dict:
        if (-1) * key in cd_dict:
            count += ab_dict[key] * cd_dict[(-1) * key]
    return count
