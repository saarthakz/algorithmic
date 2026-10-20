"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.

    Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.

    Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.rows = rows = len(board)
        self.cols = cols = len(board[0])

        # Explore O cells connected to the board's edges.
        for row in range(rows):
            self.mark_safe(row, 0)
            self.mark_safe(row, cols - 1)

        for col in range(cols):
            self.mark_safe(0, col)
            self.mark_safe(rows - 1, col)

        # Capture surrounded regions and restore safe cells.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"

    def mark_safe(self, row: int, col: int) -> None:
        if not self.in_bounds(row, col):
            return
        if self.board[row][col] != "O":
            return

        # Mark as safe and visited.
        self.board[row][col] = "S"

        neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        for next_row, next_col in neighbours:
            self.mark_safe(next_row, next_col)

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols
