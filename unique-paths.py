"""
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
"""

from typing import Dict, Tuple


class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:

        mp: Dict[Tuple[int, int], int] = {}

        return self.helper(
            rows=rows,
            cols=cols,
            row=0,
            col=0,
            mp=mp,
        )

    def helper(
        self,
        *,
        rows: int,
        cols: int,
        row: int,
        col: int,
        mp: Dict[Tuple[int, int], int]
    ):

        # Base case, destination reached
        if row == rows - 1 and col == cols - 1:
            return 1

        # Out of bounds
        if row == rows or col == cols:
            return 0

        if (row, col) in mp:
            return mp[(row, col)]

        ans = self.helper(
            rows=rows,
            cols=cols,
            row=row + 1,
            col=col,
            mp=mp,
        ) + self.helper(
            rows=rows,
            cols=cols,
            row=row,
            col=col + 1,
            mp=mp,
        )

        mp[(row, col)] = ans
        return ans
