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


@pytest.mark.parametrize("text", ["name=kek\n"])
def test_access_as_collection_and_as_attribute(temp_file):
    storage = KeyValueStorage(temp_file)
    assert storage.name == "kek"
    assert storage["name"] == "kek"


@pytest.mark.parametrize("text", ["1=kek\n"])
def test_raise_error_if_int_attribute(temp_file):
    with pytest.raises(ValueError, match="Int cant be an attribute"):
        KeyValueStorage(temp_file)


@pytest.mark.parametrize("text", ["power=9001\n"])
def test_treated_as_int(temp_file):
    assert isinstance(KeyValueStorage(temp_file).power, int)
