"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests

 * https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""

import operator
from itertools import count, cycle, islice
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    Return a generator of yielded n FizzBuzz numbers.

    Any number divisible by 3 becomes 'fizz'.
    Number divisible by 5 becomens 'buzz.
    Number divisible by both becomes 'fizzbuzz'.
    Others numbers remain the same.

    Define input and expected output:
    >>> next(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    >>> next(fizzbuzz(0))
    Traceback (most recent call last):
        ...
    ValueError: n must be > 0
    """
    if n <= 0:
        raise ValueError("n must be > 0")
    fizzes = cycle(["", "", "fizz"])
    buzzes = cycle(["", "", "", "", "buzz"])
    words = map(operator.add, fizzes, buzzes)
    numbers = map(str, count(1))
    fizzbuzz_numbers = map(max, words, numbers)
    yield list(islice(fizzbuzz_numbers, n))
