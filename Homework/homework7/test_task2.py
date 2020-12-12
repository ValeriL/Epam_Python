from homework7.task2 import backspace_compare

import pytest


@pytest.mark.parametrize(
    ["first_string", "second_string", "result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("#", "", True),
        ("abc.", "abc.#", False),
        ("a b", "a #b", False),
    ],
)
def test_backspace_compare(first_string: str, second_string: str, result: bool):
    assert backspace_compare(first_string, second_string) == result
