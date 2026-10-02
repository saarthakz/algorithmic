"""
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row = col = 0
        zero_rows = set()
        zero_cols = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in zero_rows:
            matrix[row] = [0] * cols

        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0
