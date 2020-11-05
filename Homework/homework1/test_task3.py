import io
from typing import Tuple

import pytest

from homework1.task3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("\n".join(str(x) for x in [1, 2, 3, 4, 5]), (1, 5)),
        ("\n".join(str(x) for x in [0, 0, 0, 0, 0]), (0, 0)),
        ("\n".join(str(x) for x in [56, 42, -100, 3894, 6]), (-100, 3894)),
    ],
)
def test_find_maximum_and_minimum(
    value: io.StringIO(), expected_result: Tuple[int, int]
):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
