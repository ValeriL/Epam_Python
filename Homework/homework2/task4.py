"""
Write a function that accepts another function as an argument.

Then it should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def func(a: int, b: int):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def caching(*args: int):
        if args in cache_memory:
            return cache_memory[args]
        cache_memory[args] = func(*args)
        return cache_memory[args]

    return caching
