"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

from typing import List, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.dim = 9
        self.sub_dim = 3

        for idx in range(self.dim):
            if not self.check_row(board, idx) or not self.check_col(board, idx):
                return False

        for idx in range(0, self.dim, 3):
            for _idx in range(0, self.dim, 3):
                if not self.check_sub_square(board, (idx, _idx)):
                    return False
        return True

    def check_sub_square(self, board: List[List[str]], start: Tuple[int, int]):
        row, col = start
        st = set()
        for idx in range(row, row + self.sub_dim):
            for _idx in range(col, col + self.sub_dim):
                if board[idx][_idx] == ".":
                    continue
                if board[idx][_idx] in st:
                    return False

                st.add(board[idx][_idx])
        return True

    def check_row(self, board: List[List[str]], row_idx: int):
        row_st = set()
        for col in range(self.dim):
            if board[row_idx][col] == ".":
                continue

            if board[row_idx][col] in row_st:
                return False

            row_st.add(board[row_idx][col])
        return True

    def check_col(self, board: List[List[str]], col_idx: int):
        col_st = set()
        for row in range(self.dim):
            if board[row][col_idx] == ".":
                continue

            if board[row][col_idx] in col_st:
                return False

            col_st.add(board[row][col_idx])
        return True
