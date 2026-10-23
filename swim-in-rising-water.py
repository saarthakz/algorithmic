"""
You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).
"""

from typing import List


import heapq
from typing import List, Tuple


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        # Min-heap stores: (max_elevation_so_far, row, col)
        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        while pq:
            curr_max, row, col = heapq.heappop(pq)

            if row == self.rows - 1 and col == self.cols - 1:
                return curr_max

            neighbours = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]

            for next_pos in neighbours:
                if self.in_bounds(next_pos) and next_pos not in visited:
                    visited.add(next_pos)
                    next_row, next_col = next_pos
                    next_max = max(curr_max, grid[next_row][next_col])
                    heapq.heappush(pq, (next_max, next_row, next_col))

        return -1

    def in_bounds(self, curr: Tuple[int, int]) -> bool:
        row, col = curr
        return 0 <= row < self.rows and 0 <= col < self.cols
