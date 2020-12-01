"""
Given a dictionary (tree), that can contains multiple nested structures.

Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from itertools import chain
from typing import Any, Iterable


def chain_collection(collection: Iterable):
    if isinstance(collection, dict):
        return chain.from_iterable(collection.items())
    return chain(collection)


def count_occurrences(collection: Iterable, element: Any) -> int:

    collection = chain_collection(collection)

    count = 0
    for el in collection:
        count += el == element
        if isinstance(el, (dict, tuple, list, set)):
            count += count_occurrences(el, element)

    return count


def find_occurrences(tree: dict, element: Any) -> int:

    return count_occurrences(tree, element)