"""This file contains the core logic for game of life."""

import numpy as np


def parse_from_string(board: str):
    """Parse the board from string.

    Locations marked with X and x are considered alive, all other locations are considered dead.
    """
    board = board.strip().upper()
    rows = [row.strip() for row in board.split("\n")]
    num_cols = len(rows[0])
    for row_idx, row in enumerate(rows):
        if len(row) != num_cols:
            raise ValueError(
                f"Inconsistent number of columns, first deviation in row {row_idx}: '{row}'."
            )
    return np.array([[int(cell == "X") for cell in row] for row in rows])


class Board:

    def __init__(self, board: np.ndarray):
        if board.ndim != 2:
            raise ValueError("Board must be a 2D array.")
        if board.size == 0:
            raise ValueError("Board must not be empty.")
        self._board = board

    @classmethod
    def from_string(cls, board: str):
        return cls(parse_from_string(board))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (
            "\n".join(
                ["".join(["X" if cell else "." for cell in row]) for row in self._board]
            )
            + "\n"
        )

    def __eq__(self, value: object) -> bool:
        return isinstance(value, Board) and np.array_equal(self._board, value._board)

    def evolve(self):
        # loop over a copy of board
        iter = self._board.copy()

        for i, row in enumerate(iter):
            for j, cell in enumerate(row):
                count = self.count_alive_neighbors(iter, i, j)
                if cell:
                    if count < 2 or count > 3:
                        self._board[i, j] = 0
                else:
                    if count == 3:
                        self._board[i, j] = 1

    def count_alive_neighbors(self, board, i, j):
        count = 0

        i_inc = [-1, 0, 1]
        j_inc = [-1, 0, 1]

        for id in i_inc:
            for jd in j_inc:
                _i = i + id
                _j = j + jd

                if id == 0 and jd == 0: 
                    continue

                if _i >= 0 and _i < self._board.shape[0] and _j >= 0 and _j < self._board.shape[1]:
                    if board[_i, _j]: 
                        count += 1

        return count

        
