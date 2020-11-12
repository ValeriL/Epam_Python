from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    Write a function that takes K lists as arguments.

    Returns all possible lists of K items where the first element is from the first list,
    the second is from the second and so one.
    You may assume that that every list contain at least one element
    """
    comb = [[]]
    for input_list in args:
        comb = [x + [y] for x in comb for y in input_list]
    return comb
