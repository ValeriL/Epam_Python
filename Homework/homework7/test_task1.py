from typing import Any

from homework7.task1 import find_occurrences

import pytest


@pytest.fixture()
def example_tree():

    return {
        1: [
            1,
            False,
            "string",
            [1, False, "string", {1: 1}],
            {1: 1},
            (1, False, "string"),
            {1, False, "string"},
        ],
        2: "string",
        3: [],
        4: "",
    }


@pytest.mark.parametrize(
    ["element_to_find", "number_occurrences"],
    [
        (1, 9),
        (False, 4),
        ("string", 5),
        ({1: 1}, 2),
        ({1, False, "string"}, 1),
        ((1, False, "string"), 1),
        ([1, False, "string", {1: 1}], 1),
        ("", 1),
        (5, 0),
        ([], 1),
        ({}, 0),
    ],
)
def test_find_occurrences(example_tree, element_to_find: Any, number_occurrences: int):
    assert find_occurrences(example_tree, element_to_find) == number_occurrences
