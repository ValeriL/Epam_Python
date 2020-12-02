"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).

Write a function that checks if there are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def result(winners: List) -> str:
    amount_winners = len(winners)

    if amount_winners == 1:
        return winners[0] + " wins!"
    if amount_winners == 2:
        return "draw"

    return "unfinished"


def tic_tac_toe_checker(board: List[List]) -> str:
    lined_board = sum(board, [])
    win_idx_comb = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
    ]
    winners = []

    for comb in win_idx_comb:
        cur_comb = [lined_board[idx] for idx in comb]
        cur_sign = cur_comb[0]
        if len(set(cur_comb)) == 1 and cur_sign != "-":
            winners.append(cur_sign)

    return result(winners)
