from typing import List, Tuple

from homework2.task2 import major_and_minor_elem

import pytest


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([1, 1, 3, 2, 1, 1, 1], (1, 2)),
        ([1, 1, 3, 2, 2, 1, 1, 1], (1, 3)),
    ],
)
def test_major_and_minor_elem(inp: List, expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(inp)

    assert actual_result == expected_result
