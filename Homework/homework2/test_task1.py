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


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [
        (
            "Homework/homework2/test_file.txt",
            [
                "practicality",
                "complicated",
                "readability",
                "veränderung",
                "beautiful",
                "explicit",
                "silently",
                "special",
                "simple",
                "nested",
            ],
        ),
        (
            "Homework/homework2/data.txt",
            [
                "wiederbelebungsübungen",
                "werkstättenlandschaft",
                "werkstättenlandschaft",
                "entscheidungsschlacht",
                "selbstbezichtigungen",
                "freiheitsbewusstsein",
                "geschichtsunterricht",
                "gewissenserforschung",
                "menschenfreundlichen",
                "einzelwissenschaften",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [("Homework/homework2/data.txt", "›")],
)
def test_get_rarest_char(path: str, expected_result: str):
    actual_result = get_rarest_char(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [("Homework/homework2/data.txt", 5472)],
)
def test_count_punctuation_chars(path: str, expected_result: int):
    actual_result = count_punctuation_chars(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [("Homework/homework2/data.txt", 2972)],
)
def test_count_non_ascii_chars(path: str, expected_result: int):
    actual_result = count_non_ascii_chars(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [("Homework/homework2/data.txt", "ä")],
)
def test_get_most_common_non_ascii_char(path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [
        (io.StringIO(r"...Looool \u00fc\u00fc\u00fc\u00fc\u00fc"), " "),
        (io.StringIO(r"aabbbcch"), "h"),
        (io.StringIO(r"\u00fc\u00fc\u2014\u2014\u2014"), "\u00fc"),
        (io.StringIO(r"Hoho."), "."),
    ],
)
def test_helper_get_rarest_char(line: str, expected_result: str):
    actual_result = _get_rarest_char(line)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [(io.StringIO(r".Magic!,\u00fc"), 3), (io.StringIO(r"When september ends"), 0)],
)
def test_helper_punctuation_chars(line: str, expected_result: int):
    actual_result = _count_punctuation_chars(line)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [
        (io.StringIO(r"\u2014Magic! \u00fc\u00fc"), 3),
        (io.StringIO(r"Happy Birthday"), 0),
    ],
)
def test_helper_count_non_ascii_chars(line: str, expected_result: int):
    actual_result = _count_non_ascii_chars(line)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["line", "expected_result"],
    [
        (
            io.StringIO(r"\u2014\u00fc\u00fc Looooool...... \u00fc\u00fc\u00fc"),
            "\u00fc",
        ),
        (io.StringIO(r"Maaaaaaaagician"), ""),
        (io.StringIO(r"\u00fc\u00fc\u2014 \u2014\u2014"), "\u2014"),
    ],
)
def test_helper_get_most_common_non_ascii_char(line: str, expected_result: str):
    actual_result = _get_most_common_non_ascii_char(line)
    assert actual_result == expected_result
