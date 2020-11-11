import io
from typing import List

from homework2.task1_text import (
    _count_non_ascii_chars,
    _count_punctuation_chars,
    _get_most_common_non_ascii_char,
    _get_rarest_char,
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

import pytest

file_path = "Homework/homework2/data.txt"


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [
        (
            "Homework/homework2/test_file.txt",
            [
                "abcdefghijk",
                "veränderung",
                "abcdefghij",
                "abcdefghi",
                "abcdefgh",
                "abcdefg",
                "abcdef",
                "abcde",
                "abcd",
                "abc",
            ],
        ),
        (
            "Homework/homework2/data.txt",
            [
                "werkstättenlandschaft",
                "unmissverständliche",
                "bevölkerungsabschub",
                "kollektivschuldiger",
                "friedensabstimmung",
                "ausserordentliche",
                "schicksalsfiguren",
                "grosskampfmittel",
                "vorausgeschickt",
                "fingerabdrucks",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(path)
    assert actual_result == expected_result


def test_get_rarest_char():
    assert get_rarest_char(file_path) == "›"


def test_count_punctuation_chars():
    assert count_punctuation_chars(file_path) == 5472


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(file_path) == 2972


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(file_path) == "ä"


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [
        (r"...Looool \u00fc\u00fc\u00fc\u00fc\u00fc", " "),
        (r"aabbbcch", "h"),
        (r"\u00fc\u00fc\u2014\u2014\u2014", "\u00fc"),
        (r"Hoho.", "."),
    ],
)
def test_helper_get_rarest_char(line: str, expected_result: str):
    actual_result = _get_rarest_char(io.StringIO(line))
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [(r".Magic!,\u00fc", 3), (r"When september ends", 0)],
)
def test_helper_punctuation_chars(line: str, expected_result: int):
    actual_result = _count_punctuation_chars(io.StringIO(line))
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [
        (r"\u2014Magic! \u00fc\u00fc", 3),
        (r"Happy Birthday", 0),
    ],
)
def test_helper_count_non_ascii_chars(line: str, expected_result: int):
    actual_result = _count_non_ascii_chars(io.StringIO(line))
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [
        (
            r"\u2014\u00fc\u00fc Looooool...... \u00fc\u00fc\u00fc",
            "\u00fc",
        ),
        (r"Maaaaaaaagician", ""),
        (r"\u00fc\u00fc\u2014 \u2014\u2014", "\u2014"),
    ],
)
def test_helper_get_most_common_non_ascii_char(line: str, expected_result: str):
    actual_result = _get_most_common_non_ascii_char(io.StringIO(line))
    assert actual_result == expected_result
