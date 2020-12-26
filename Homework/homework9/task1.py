"""
Write a function that merges integer from sorted files and returns an iterator.

file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Generator, Iterator, List, Union


def next_element(iterator: Generator):
    try:
        return next(iterator)
    except StopIteration:
        return None


def merge_two_files(  # noqa : CCR001 7 > 5
    iterator1: Generator, iterator2: Generator
) -> int:
    number1 = next_element(iterator1)
    number2 = next_element(iterator2)
    while number1 is not None or number2 is not None:
        if number1 is None:
            yield number2
            number2 = next_element(iterator2)
        elif number2 is None:
            yield number1
            number1 = next_element(iterator1)
        elif number1 >= number2:
            yield number2
            number2 = next_element(iterator2)
        elif number1 < number2:
            yield number1
            number1 = next_element(iterator1)


def read_file(path: Union[Path, str]) -> int:
    with open(path, "r") as file:
        for line in file:
            yield int(line)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    file_iter = iter(file_list)
    merged_files = read_file(next_element(file_iter))
    next_file = next_element(file_iter)
    while next_file is not None:
        merged_files = merge_two_files(merged_files, read_file(next_file))
        next_file = next_element(file_iter)
    yield from merged_files
