"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*.

Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!" <- lol :D
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:  # noqa
    """
    Return a list of n FizzBuzz numbers.

    Any number divisible by 3 becomes 'fizz'.
    Number divisible by 5 becomens 'buzz.
    Number divisible by both becomes 'fizzbuzz'.
    Others numbers remain the same.

    Define input and expected output:
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    >>> fizzbuzz(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be > 0
    """
    if n <= 0:
        raise ValueError("n must be > 0")
    fizzbuzz_numbers = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizzbuzz_numbers.append("fizzbuzz")
        elif i % 3 == 0:
            fizzbuzz_numbers.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_numbers.append("buzz")
        else:
            fizzbuzz_numbers.append(str(i))
    return fizzbuzz_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
