import os

from homework4.task1 import read_magic_number

import pytest


path = "Homework/homework4/test.txt"


@pytest.fixture()
def _del_file():
    with open(path, "w") as test_file:
        test_file.write("abc")
    yield
    os.remove(path)


def test_file_existence_error():
    with pytest.raises(ValueError, match="No such file"):
        read_magic_number("any_file.txt")


@pytest.mark.usefixtures("_del_file")
def test_not_a_number_error():
    with pytest.raises(ValueError, match="Not a number"):
        read_magic_number(path)


@pytest.mark.parametrize(
    ["num", "expected_result"],
    [("0", False), ("1", True), ("3", False), ("7.56", False)],
)
@pytest.mark.usefixtures("_del_file")
def test_read_magic_number(num: str, expected_result: bool):
    with open(path, "w") as test_file:
        test_file.write(num)
    assert read_magic_number(path) == expected_result
