"""
Given a dictionary (tree), that can contains multiple nested structures.

Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable


def find_occurrences(tree: Iterable, element: Any) -> int:

    if isinstance(tree, dict):
        tree = tree.items()
    count = 0
    for el in tree:
        count += el == element
        if isinstance(el, (dict, tuple, list, set)):
            count += find_occurrences(el, element)
    return count
