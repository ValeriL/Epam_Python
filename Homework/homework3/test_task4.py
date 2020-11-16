from homework3.task4 import is_armstrong

import pytest


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(9, True), (10, False), (153, True), (0, True), (1, True)],
)
def test_is_armstrong(value: int, expected_result: bool):
    actual_result = is_armstrong(value)

    assert actual_result == expected_result
