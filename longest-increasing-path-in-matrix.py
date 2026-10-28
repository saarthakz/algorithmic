"""
You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

Return the length of the longest strictly increasing path within matrix.

From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.
"""

from typing import List, Tuple, Dict, Set


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        visited = set()
        mp = {}

        max_path_len = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in visited:
                    continue

                max_path_len = max(
                    max_path_len, self.helper(matrix, row, col, visited, mp)
                )

        return max_path_len

    def helper(
        self,
        matrix: List[List[int]],
        row: int,
        col: int,
        visited: Set[Tuple[int, int]],
        mp: Dict[Tuple[int, int], int],
    ):
        if (row, col) in visited:
            return 0

        if (row, col) in mp:
            return mp[(row, col)]

        visited.add((row, col))

        neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        max_path_len = 1

        for next_row, next_col in neighbours:
            if (
                self.in_bound(next_row, next_col)
                and matrix[next_row][next_col] > matrix[row][col]
            ):
                max_path_len = max(
                    max_path_len,
                    1 + self.helper(matrix, next_row, next_col, visited, mp),
                )

        visited.remove((row, col))

        mp[(row, col)] = max_path_len

        return max_path_len

    def in_bound(self, row: int, col: int):
        return 0 <= row < self.rows and 0 <= col < self.cols
