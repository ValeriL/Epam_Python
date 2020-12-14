import os
import shutil
from pathlib import Path
from typing import Callable, Optional

from homework9.task3 import universal_file_counter

import pytest


@pytest.fixture()
def dir_path(text1: str, text2: str):
    path = "Homework/homework9/test_files"
    os.mkdir(path)
    with open(os.path.join(path, "file1.txt"), "w+") as file:
        file.write(text1)
    with open(os.path.join(path, "file2.txt"), "w+") as file:
        file.write(text2)
    yield Path(path)
    shutil.rmtree(path)


@pytest.mark.parametrize(
    ["text1", "text2", "tokenizer", "token_count"],
    [
        ("line1\nline2", "line3", None, 3),
        ("line 1\nline 2", "line3", str.split, 5),
        ("", "", None, 0),
        ("", "", str.strip, 0),
    ],
)
def test_universal_file_counter(
    dir_path, tokenizer: Optional[Callable], token_count: int
):

    assert universal_file_counter(dir_path, "txt", tokenizer) == token_count
