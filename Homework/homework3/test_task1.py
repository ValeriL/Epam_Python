from unittest.mock import Mock

from homework3.task_1 import cache

import pytest


@pytest.mark.parametrize(
    "times,calls,expected_result", [(1, 4, 2), (2, 4, 2), (3, 4, 1), (3, 5, 2)]
)
def test_cache(times: int, calls: int, expected_result: int):

    mock = Mock()
    cache_call = cache(times)(mock)

    for _ in range(0, calls):
        cache_call()

    assert mock.call_count == expected_result
