"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:

    0 representing an empty cell
    1 representing a fresh fruit
    2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
"""

from typing import List, Deque, Tuple
from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue: Deque[Tuple[int, int, int]] = deque()
        self.rows = len(grid)
        self.cols = len(grid[0])
        fresh_cnt = 0
        max_minute = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    fresh_cnt += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))

        while len(queue):
            row, col, minute = queue.popleft()

            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]

            for next_row, next_col in neighbors:
                if self.in_bounds(next_row, next_col) and grid[next_row][next_col] == 1:
                    # Mark directly here to prevent identical cells entering queue
                    grid[next_row][next_col] = 2
                    fresh_cnt -= 1
                    max_minute = minute + 1
                    queue.append((next_row, next_col, minute + 1))

        return -1 if fresh_cnt else max_minute

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols
