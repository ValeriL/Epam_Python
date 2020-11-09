from typing import Any, List

from homework2.task3 import combinations

import pytest


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (([1], [2], [3]), [[1, 2, 3]]),
        (([0, 0], [0]), [[0, 0]]),
    ],
)
def test_combinations(args: List[Any], expected_result: List[List]):
    actual_result = combinations(*args)

    assert actual_result == expected_result
