from unittest.mock import Mock

from homework3.task_1 import cache

import pytest


@pytest.mark.parametrize("times,expected_result", [(1, 2), (2, 2), (3, 1)])
def test_cache(times: int, expected_result: int):

    mock = Mock()
    cache_call = cache(times)(mock)

    cache_call()
    cache_call()
    cache_call()
    cache_call()

    assert mock.call_count == expected_result
