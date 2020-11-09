import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    Write a function that takes K lists as arguments.

    Returns all possible lists of K items where the first element is from the first list,
    the second is from the second and so one.
    You may assume that that every list contain at least one element

    Combinations are not repeated
    """
    comb_tuple = list(itertools.product(*args))
    comb_list = [list(comb) for comb in comb_tuple]
    comb_list_no_rep = []
    for el in comb_list:
        if el not in comb_list_no_rep:
            comb_list_no_rep.append(el)
    return comb_list_no_rep
