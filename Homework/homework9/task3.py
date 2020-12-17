"""
Write a function that takes directory path, a file extension and an optional tokenizer.

It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
import fileinput
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(  # noqa : CCR001
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:

    token_count = 0
    for path in dir_path.glob("**/*" + file_extension):
        if tokenizer:
            with open(path, "r") as file:
                file_input = file.read()
            if file_input:
                token_count += sum(1 for token in tokenizer(file_input))
        else:
            token_count += sum(1 for _ in fileinput.input(path))
    return token_count
