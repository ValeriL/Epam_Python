from typing import Any, Iterable, List


def custom_range(
    input_line: Iterable, stop: Any, start: Any = None, step: int = 1
) -> List[Any]:
    """
    Write a function that accept any iterable of unique values and then it behaves as range function.

    Some of the functions have a bit cumbersome behavior when we deal with positional and keyword arguments.
    import string
    assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
    assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
    """
    if start is not None:
        stop, start = start, stop
    if start is None:
        start = input_line[0]

    start_ind = input_line.index(start)
    stop_ind = input_line.index(stop)
    return list(input_line[start_ind:stop_ind:step])
