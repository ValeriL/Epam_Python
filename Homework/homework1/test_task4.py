from typing import List

import pytest

from homework1.task4 import check_sum_of_four


@pytest.mark.parametrize(
    ["val1", "val2", "val3", "val4", "expected_result"],
    [
        ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 81),
        ([1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], 0),
        ([], [], [], [], 0),
        ([1, 1, 1], [2, 2, 2], [0, 0, 0], [-3, -3, -3], 81),
        ([1, 2, 3], [1, 2, 3], [-1, -2, -3], [-1, -2, -3], 19),
    ],
)
def test_check_sum_of_four(
    val1: List[int],
    val2: List[int],
    val3: List[int],
    val4: List[int],
    expected_result: int,
):
    actual_result = check_sum_of_four(val1, val2, val3, val4)

    assert actual_result == expected_result
