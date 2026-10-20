"""
You are given a m x n 2D grid initialized with these three possible values:

    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""

from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.rows, self.cols = len(grid), len(grid[0])

        queue = deque()
        INF = 2147483647

        # Collect all treasure chests for Multi-source BFS
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        # Multi Source BFS
        while queue:
            row, col = queue.popleft()

            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]

            for next_row, next_col in neighbors:
                if (
                    self.in_bounds(next_row, next_col)
                    and grid[next_row][next_col] == INF
                ):
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row, next_col))

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols
