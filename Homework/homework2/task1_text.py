import io
import string
from typing import List, Mapping, Tuple

punctuation = string.punctuation + "\u2014" + "\u00bb" + "\u00ab"


def u_decoder(line: str) -> str:
    """Decode ascii chars."""
    return line.encode().decode("unicode-escape")


def remove_punctuation_and_decode(line: str) -> str:
    """
    Decode, remove punctuation from the string.

    Add a long dash and angle quotes to a punctuation.
    """
    map_char = str.maketrans(punctuation, " " * len(punctuation))
    return u_decoder(line).translate(map_char).casefold()


def _get_max_unique_chars_word(
    word: str, max_word: str, max_len: int
) -> Tuple[str, int]:
    """Get the word with the greatest amount of unique chars."""
    cur_len = len(set(word))
    if max_len < cur_len:
        max_len = cur_len
        max_word = word
    return max_word, max_len


def _sort_words_list(long_words: List[str]) -> List[str]:
    """Sort by an amount of unique chars and then by length."""
    long_words.sort(key=lambda s: len(set(s)), reverse=True)
    long_words_slice = long_words[0:10]
    long_words_slice.sort(key=lambda s: len(s), reverse=True)
    return long_words_slice


def get_max_word(line: str, words_list: List[str]) -> str:
    """Get the word with the max amount of unique chars from the line."""
    max_word = ""
    max_len = 0
    words = remove_punctuation_and_decode(line).strip().split()
    for word in words:
        if word not in words_list:
            max_word, max_len = _get_max_unique_chars_word(word, max_word, max_len)
    return max_word


def _get_longest_diverse_words(file: io.StringIO()) -> List[str]:
    long_words = []
    for line in file:
        long_words.append(get_max_word(line, long_words))
    return _sort_words_list(long_words)


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from the largest amount of unique symbols."""
    with open(file_path, "r") as file:
        return _get_longest_diverse_words(file)


def _get_rarest_char(file: io.StringIO()) -> str:
    char_count = {}
    for line in file:
        for ch in u_decoder(line).strip().lower():
            _update_char_dict(ch, char_count)
    return min(char_count, key=char_count.get)


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document."""
    with open(file_path, "r") as file:
        return _get_rarest_char(file)


def _count_punctuation_chars(file: io.StringIO()) -> int:
    count = 0
    for line in file:
        for sym in punctuation:
            count += u_decoder(line).strip().count(sym)
    return count


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char."""
    with open(file_path, "r") as file:
        return _count_punctuation_chars(file)


def calc_non_ascii(line: str) -> int:
    """Calculate non ascii chars in the line."""
    return sum(ch not in string.printable for ch in u_decoder(line).strip())


def _count_non_ascii_chars(file: io.StringIO()) -> int:
    count = 0
    for line in file:
        count += calc_non_ascii(line)
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char."""
    with open(file_path, "r") as file:
        return _count_non_ascii_chars(file)


def _update_char_dict(ch: str, char_dict: Mapping[str, int]) -> Mapping[str, int]:
    """Update char dictionary: add key (char) or increase a value."""
    if ch in char_dict:
        char_dict[ch] += 1
    else:
        char_dict[ch] = 1


def _update_counter(line: str, char_dict: Mapping[str, int]) -> Mapping[str, int]:
    """Add a char to char_count dict or add one to amount of repeats."""
    for ch in u_decoder(line).strip():
        if ch not in string.printable:
            _update_char_dict(ch, char_dict)
    return char_dict


def _get_most_common_non_ascii_char(file: io.StringIO()) -> str:
    char_count = {}
    for line in file:
        _update_counter(line, char_count)
    if not bool(char_count):
        return ""
    return max(char_count, key=char_count.get)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for the document."""
    with open(file_path, "r") as file:
        return _get_most_common_non_ascii_char(file)
