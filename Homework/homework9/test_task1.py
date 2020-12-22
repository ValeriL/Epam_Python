import os

from homework9.task1 import merge_sorted_files

import pytest


@pytest.fixture()
def temp_files(text1: str, text2: str, text3: str):
    path1 = "Homework/homework9/test1.txt"
    path2 = "Homework/homework9/test2.txt"
    path3 = "Homework/homework9/test3.txt"
    with open(path1, "w+") as test_file:
        test_file.write(text1)
    with open(path2, "w+") as test_file:
        test_file.write(text2)
    with open(path3, "w+") as test_file:
        test_file.write(text3)
    yield [path1, path2, path3]
    os.remove(path1)
    os.remove(path2)
    os.remove(path3)


@pytest.mark.parametrize(
    ["text1", "text2", "text3", "result"],
    [
        ("1\n3\n5", "2\n7", "4\n6", [1, 2, 3, 4, 5, 6, 7]),
        ("", "", "", []),
        ("1\n1", "1\n1\n1", "1", [1, 1, 1, 1, 1, 1]),
    ],
)
def test_merge_sorted_files(temp_files, result):
    assert list(merge_sorted_files(temp_files)) == result
