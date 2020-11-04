import io
from typing import Tuple

import pytest

from homework1.task3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (io.StringIO("\n".join(str(x) for x in [1, 2, 3, 4, 5])), (1, 5)),
        (io.StringIO("\n".join(str(x) for x in [0, 0, 0, 0, 0])), (0, 0)),
        (io.StringIO("\n".join(str(x) for x in [-100, 42, 56, 3894, 6])), (-100, 3894)),
    ],
)
def test_find_maximum_and_minimum(
    value: io.StringIO(), expected_result: Tuple[int, int]
):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
