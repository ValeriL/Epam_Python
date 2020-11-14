from typing import List

from homework2.task4 import cache


def test_cache_1():
    def func(a: int, b: int) -> int:
        return a * b

    cache_func = cache(func)
    some = 100, 200

    val1 = cache_func(*some)
    val2 = cache_func(*some)

    assert val1 is val2


def test_cache_2():
    def foo(a=10) -> int:
        return 3 + a

    cache_func = cache(foo)

    val1 = cache_func(a=1)
    val2 = cache_func(a=1)

    assert val1 is val2


def test_cache_3():
    def boo(nums: List[int]) -> int:
        return sum(x + 1 for x in nums)

    cache_func = cache(boo)
    nums_list = [1, 2, 3]

    val1 = cache_func(nums_list)
    val2 = cache_func(nums_list)

    assert val1 is val2


def test_cache_4():
    def foo(a=10) -> int:
        return 3 + a

    cache_func = cache(foo)

    val1 = cache_func(a=1)
    val2 = cache_func(a=1)

    assert val1 is val2
