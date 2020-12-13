import os

from homework8.task1 import KeyValueStorage

import pytest


@pytest.fixture()
def temp_file(text: str):
    path = "Homework/homework8/test.txt"
    with open(path, "w") as test_file:
        test_file.write(text)
    yield path
    os.remove(path)


@pytest.mark.parametrize(
    ["text", "value"],
    [
        ("name=kek\n", "kek"),
        ("name=kek==kek\n", "kek==kek"),
        ("name=kek\tkek\n", "kek\tkek"),
    ],
)
def test_access_as_collection_and_as_attribute(temp_file, value):
    storage = KeyValueStorage(temp_file)
    assert storage.name == value
    assert storage["name"] == value


@pytest.mark.parametrize("text", ["1=kek\n", "def=kek\n"])
def test_raise_error_if_int_attribute(temp_file):
    with pytest.raises(ValueError, match="Cant be an attribute"):
        KeyValueStorage(temp_file)


@pytest.mark.parametrize("text", ["power=9001\n"])
def test_treated_as_int(temp_file):
    assert isinstance(KeyValueStorage(temp_file).power, int)
