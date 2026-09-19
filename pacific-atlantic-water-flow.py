"""
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.
"""

from typing import List, Tuple, Set


class Solution:
    def pacificAtlantic(self, islands: List[List[int]]) -> List[List[int]]:

        rows = len(islands)
        cols = len(islands[-1])

        self.islands = islands

        self.rows = rows
        self.cols = cols

        visited = set()
        self.ocean_map = {}

        for row in range(rows):
            for col in range(cols):
                self.ocean_map[(row, col)] = [0, 0]  # Pacific, Atlantic

        for row in range(rows):
            self.ocean_map[(row, 0)][0] = 1  # All the left islands touch the pacific
            self.ocean_map[(row, cols - 1)][
                1
            ] = 1  # All the right islands touch the atlantic

        for col in range(cols):
            self.ocean_map[(0, col)][0] = 1  # All the top islands touch the pacific
            self.ocean_map[(rows - 1, col)][
                1
            ] = 1  # All the bottom islands touch the atlantic

        for row in range(rows):
            for col in range(cols):
                self.helper(
                    row,
                    col,
                    visited,
                )

        ans = []
        for key in self.ocean_map.keys():
            if tuple(self.ocean_map[key]) == (1, 1):
                ans.append(list(key))

        return ans

    def in_bounds(self, row: int, col: int):
        return (row >= 0 and row < self.rows) and (col >= 0 and col < self.cols)

    def is_flow_possible(self, curr_row, curr_col, tg_row, tg_col):
        curr_val = self.islands[curr_row][curr_col]
        tg_val = self.islands[tg_row][tg_col]

        return curr_val >= tg_val

    def helper(
        self,
        row: int,
        col: int,
        visited: set[Tuple[int, int]],
    ) -> List[int]:

        # Base case
        if (row, col) in visited:
            return self.ocean_map[(row, col)]

        # Add current island to visited set
        visited.add((row, col))

        neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        for n_row, n_col in neighbours:
            # If unvisited, flow possible neighbour in bound
            if self.in_bounds(n_row, n_col) and self.is_flow_possible(
                row, col, n_row, n_col
            ):
                pac_flag, atl_flag = self.helper(
                    n_row,
                    n_col,
                    visited,
                )

                curr_pac_flag, curr_atl_flag = self.ocean_map[(row, col)]

                curr_pac_flag = curr_pac_flag or pac_flag
                curr_atl_flag = curr_atl_flag or atl_flag

                self.ocean_map[(row, col)] = [curr_pac_flag, curr_atl_flag]

        return self.ocean_map[(row, col)]
