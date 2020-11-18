import os

from homework4.task1 import read_magic_number

import pytest


@pytest.fixture()
def open_del_file(text: str):
    path = "Homework/homework4/test.txt"
    with open(path, "w") as test_file:
        test_file.write(text)
    yield path
    os.remove(path)


def test_file_existence_error():
    with pytest.raises(ValueError, match="No such file"):
        read_magic_number("any_file.txt")


@pytest.mark.parametrize("text", ["abc", "12abc"])
def test_not_a_number_error(open_del_file):
    with pytest.raises(ValueError, match="Not a number"):
        read_magic_number(open_del_file)


@pytest.mark.parametrize(
    ["text", "expected_result"],
    [("0", False), ("1", True), ("3", False), ("7.56", False)],
)
def test_read_magic_number(open_del_file, expected_result: bool):
    assert read_magic_number(open_del_file) == expected_result
