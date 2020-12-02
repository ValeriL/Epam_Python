from typing import List

from homework7.task3 import tic_tac_toe_checker

import pytest


@pytest.mark.parametrize(
    ["board", "result"],
    [
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished"),
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["-", "o", "x"], ["-", "x", "o"], ["x", "-", "-"]], "x wins!"),
        ([["x", "-", "o"], ["x", "x", "o"], ["-", "-", "o"]], "o wins!"),
        ([["x", "x", "x"], ["o", "o", "o"], ["-", "-", "-"]], "draw"),
    ],
)
def test_tic_tac_toe_checker(board: List[List], result: str):
    assert tic_tac_toe_checker(board) == result
