from homework8.task2 import TableData


import pytest


@pytest.fixture()
def presidents():
    return TableData("Homework/homework8/test.sqlite", "presidents")


def test_len(presidents):
    assert len(presidents) == 3


def test_getitem(presidents):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains(presidents):
    assert ("Yeltsin" in presidents) is True
    assert ("Putin" in presidents) is False


def test_iterable(presidents):
    assert [president[0] for president in presidents] == [
        "Yeltsin",
        "Trump",
        "Big Man Tyrone",
    ]


def test_raise_error_item_not_found(presidents):
    with pytest.raises(KeyError, match="Putin not found"):
        presidents["Putin"]
