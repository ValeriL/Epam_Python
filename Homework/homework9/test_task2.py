from homework9.task2 import Suppressor, suppressor

import pytest


def test_suppressor_class_given_case():
    with Suppressor(IndexError):
        assert [][2]


def test_suppressor_class_subclasses_of_passed_exception():
    with Suppressor(BaseException):
        raise Exception("Hello")
    with Suppressor(BaseException):
        raise ZeroDivisionError


def test_suppressor_class_exception_raised_if_exception_not_in_suppressor():
    with Suppressor(IndexError):
        with pytest.raises(ZeroDivisionError):
            5 / 0


def test_suppressor_generator_given_case():
    with suppressor(IndexError):
        assert [][2]


def test_suppressor_generator_subclasses_of_passed_exception():
    with suppressor(BaseException):
        raise Exception("Hello")
    with Suppressor(BaseException):
        raise ZeroDivisionError


def test_suppressor_generator_exception_raised_if_exception_not_in_suppressor():
    with suppressor(IndexError):
        with pytest.raises(ZeroDivisionError):
            5 / 0
