from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.num_islands = 0
        self.grid = grid

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.num_islands += 1
                    self._helper(row, col)

        return self.num_islands

    def _helper(self, row: int, col: int):
        # Boundary check
        if not self._in_bound(row, col):
            return

        # If visited already, do not check
        if (row, col) in self.visited:
            return

        # Add to visited
        self.visited.add((row, col))

        # Check water spot
        if self.grid[row][col] == "0":
            return

        # Now that we know it is an unvisited piece of land,

        # And we can scan how far it spans
        possible_neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        for next_row, next_col in possible_neighbours:
            self._helper(next_row, next_col)

        return

    def _in_bound(self, row: int, col: int) -> bool:
        return row >= 0 and row < self.rows and col >= 0 and col < self.cols
