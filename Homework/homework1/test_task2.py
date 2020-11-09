from typing import Sequence

import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], True),
        ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], True),
        ([0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], False),
        ([54, 35, 67, 70], False),
        ([89, 144, 233, 377, 610, 987], False),
        ([0, 0, 0, 0, 0, 0], False),
        ([2, 5], False),
        ([0, 1], False),
        ([1, 1], False),
        ([0, 1, 1], True),
        ([1, 1, 2], True),
        ([0, 1, 2], False),
        ([1, 1, 3], False),
        ([5, 6, 3], False),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
