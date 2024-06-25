import unittest
import numpy as np
from game_of_life import lib


# fmt: off
STATIONARY_BOARD = """
....
.xx.
.xx.
....
"""
# fmt: on


class TestParseFromString(unittest.TestCase):
    def test_valid_input(self):
        input_string = "...X\n.XX.\nX..."
        expected_output = np.array([[0, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 0]])
        np.testing.assert_almost_equal(
            lib.parse_from_string(input_string), expected_output
        )

    def test_valid_input2(self):
        input_string = "-x\nxx\n--"
        expected_output = np.array([[0, 1], [1, 1], [0, 0]])
        np.testing.assert_almost_equal(
            lib.parse_from_string(input_string), expected_output
        )

    def test_invalid_input(self):
        input_string = ".\n.XX.\nX..."  # Not consistent number of columns.
        with self.assertRaises(ValueError):
            lib.parse_from_string(input_string)


class TestEvolution(unittest.TestCase):

    def test_stationary_board(self):
        board = lib.Board.from_string(STATIONARY_BOARD)
        board.evolve()
        self.assertEqual(board, lib.Board.from_string(STATIONARY_BOARD))

    def test_yourtests(self):
        pass  # Add tests as needed.


if __name__ == "__main__":
    unittest.main()
