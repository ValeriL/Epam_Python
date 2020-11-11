import io
import string
from typing import List, Mapping, Tuple


def u_decoder(line: str) -> str:
    """Decode ascii chars."""
    return line.encode().decode("unicode-escape")


def decoded_line_without_punc(line: str) -> str:
    """
    Decode, remove punctuation from the string.

    Add a long dash and angle quotes to a punctuation.
    """
    punctuation = string.punctuation + "\u2014" + "\u00bb" + "\u00ab"
    map_char = str.maketrans(punctuation, " " * len(punctuation))
    return u_decoder(line).translate(map_char).casefold()


def _find_word_max_unique(word: str, max_word: str, max_len: int) -> Tuple[str, int]:
    cur_len = len(set(word))
    if max_len < cur_len:
        max_len = cur_len
        max_word = word
    return max_word, max_len


def _get_longest_diverse_words(file: io.StringIO()) -> List[str]:
    long_words = []
    for line in file:
        max_word = ""
        max_len = 0
        words = decoded_line_without_punc(line).strip().split()
        for word in words:
            max_word, max_len = _find_word_max_unique(word, max_word, max_len)
        long_words.append(max_word)
    long_words.sort(key=lambda s: len(s), reverse=True)
    file.close()
    return long_words[1:11]


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from the largest amount of unique symbols."""
    file = open(file_path, "r")
    return _get_longest_diverse_words(file)


def _get_rarest_char(file: io.StringIO()) -> str:
    char_count = {}
    for line in file:
        for ch in u_decoder(line).strip().lower():
            char_count = _add_char_dict(ch, char_count)
    return min(char_count, key=char_count.get)


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document."""
    file = open(file_path, "r", encoding="utf-8")
    return _get_rarest_char(file)


def _count_punctuation_chars(file: io.StringIO()) -> int:
    count = 0
    punctuation = string.punctuation + "\u2014" + "\u00bb" + "\u00ab"
    for line in file:
        for sym in punctuation:
            count += u_decoder(line).strip().count(sym)
    file.close()
    return count


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char."""
    file = open(file_path, "r")
    return _count_punctuation_chars(file)


def _add_non_ascii_char(ch: str, count: int) -> int:
    """Add one if the input char is not ascii one."""
    if ch not in string.printable:
        count += 1
    return count


def _count_non_ascii_chars(file: io.StringIO()) -> int:
    count = 0
    for line in file:
        for ch in u_decoder(line).strip():
            count = _add_non_ascii_char(ch, count)
    file.close()
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char."""
    file = open(file_path, "r")
    return _count_non_ascii_chars(file)


def _add_char_dict(ch: str, char_dict: Mapping[str, int]) -> Mapping[str, int]:
    if ch in char_dict:
        char_dict[ch] += 1
    else:
        char_dict[ch] = 1
    return char_dict


def _add_non_ascii_char_dict(
    ch: str, char_dict: Mapping[str, int]
) -> Mapping[str, int]:
    """Add a char to char_count dict or add one to amount of repeats."""
    if ch not in string.printable:
        return _add_char_dict(ch, char_dict)
    return char_dict


def _get_most_common_non_ascii_char(file: io.StringIO()) -> str:
    char_count = {}
    for line in file:
        for ch in u_decoder(line).strip():
            char_count = _add_non_ascii_char_dict(ch, char_count)
    if not bool(char_count):
        return ""
    file.close()
    return max(char_count, key=char_count.get)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document."""
    file = open(file_path, "r")
    return _get_most_common_non_ascii_char(file)
