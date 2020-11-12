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
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = []

    def caching(*args):
        for stored_args, result in cache_memory:
            if stored_args == args:
                return result
        result = func(*args)
        cache_memory.append((args, result))
        return result

    return caching
