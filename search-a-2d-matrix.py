"""
You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""

from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        first_col = [row[0] for row in matrix]

        row_idx = bisect.bisect_left(first_col, target)

        # If the element is right in the first column
        if row_idx < rows and first_col[row_idx] == target:
            return True

        # Since it is not in the first column, and we did bisect_left, we will need, check the previous row
        if row_idx == 0:
            return False

        # Row of concern
        elem_idx = bisect.bisect_left(matrix[row_idx - 1], target)

        if elem_idx < cols and matrix[row_idx - 1][elem_idx] == target:
            return True
        return False
