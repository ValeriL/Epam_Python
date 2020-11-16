from typing import Callable


def cache(times: int) -> Callable:  # noqa
    def decorator(func: Callable) -> Callable:  # noqa
        cache_memory = []

        def caching(*args, **kwargs):  # noqa
            cur_input = (args, kwargs)
            for stored_args, result, count_times in cache_memory:
                if stored_args == cur_input:
                    cache_memory.remove((stored_args, result, count_times))
                    if count_times < times:
                        cache_memory.append((stored_args, result, count_times + 1))
                        return result
            result = func(*args, **kwargs)
            cache_memory.append((cur_input, result, 0))
            return result

        return caching

    return decorator
