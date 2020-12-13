from homework9.task2 import Suppressor, suppressor

import pytest


def test_suppressor_class():
    with Suppressor(IndexError):
        assert [][2]


def test_suppressor_class_exception_raised_if_exception_not_in_suppressor():
    with Suppressor(IndexError):
        with pytest.raises(ZeroDivisionError):
            5 / 0


def test_suppressor_generator():
    with suppressor(IndexError):
        assert [][2]


def test_suppressor_generator_exception_raised_if_exception_not_in_suppressor():
    with suppressor(IndexError):
        with pytest.raises(ZeroDivisionError):
            5 / 0
