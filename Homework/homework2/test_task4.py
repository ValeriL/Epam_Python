import timeit

from homework2.task4 import cache, func

import pytest


@pytest.mark.parametrize(
    ["some", "expected_result"],
    [
        ((150, 150), True),
    ],
)
def test_cache(some: int, expected_result: bool):
    cache_func = cache(func)

    val1 = cache_func(*some)
    val2 = cache_func(*some)

    time1 = timeit.timeit("cache(func(150,150))", globals=globals())
    time2 = timeit.timeit("cache(func(150,150))", globals=globals())

    actual_result = (val1 == val2) and (time2 < time1)

    assert actual_result == expected_result
