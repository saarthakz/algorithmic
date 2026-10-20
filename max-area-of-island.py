"""
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.
"""

from typing import List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited: Set[Tuple[int, int]] = set()
        self.grid = grid
        max_area = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    max_area = max(self._helper(row, col), max_area)
        return max_area

    def _helper(self, row: int, col: int):
        # Boundary check
        if not self.in_bound(row, col):
            return 0

        # If visited already, do not check
        if (row, col) in self.visited:
            return 0

        # Add to visited
        self.visited.add((row, col))

        # Check water spot
        if self.grid[row][col] == 0:
            return 0

        # Now that we know it is an unvisited piece of land,

        # And we can scan how far it spans
        possible_neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        area = 1

        for next_row, next_col in possible_neighbours:
            area += self._helper(next_row, next_col)

        return area

    def in_bound(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols
