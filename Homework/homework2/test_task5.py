import string
from typing import Any, List

from homework2.task5 import custom_range

import pytest


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        (
            (string.ascii_lowercase, "g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
        (([1, 2, 3, 4, 5, 6], 2, 6, 2), [2, 4]),
    ],
)
def test_custom_range(args: Any, expected_result: List[Any]):

    actual_result = custom_range(*args)

    assert actual_result == expected_result
