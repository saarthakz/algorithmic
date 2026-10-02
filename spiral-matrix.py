"""
Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        spiral_order = []
        row_st = 0
        col_st = 0
        while row_st < rows / 2 and col_st < cols / 2:

            top_row = row_st
            bottom_row = rows - 1 - row_st
            right_col = cols - 1 - col_st
            left_col = col_st

            # Top row
            for col in range(left_col, right_col):
                spiral_order.append(matrix[top_row][col])

            # Right column (top to bottom)
            if top_row == bottom_row:
                spiral_order.append(matrix[top_row][right_col])
            else:
                for row in range(top_row, bottom_row):
                    spiral_order.append(matrix[row][right_col])

            # Bottom row (right to left)
            if top_row != bottom_row:
                if right_col == left_col:
                    spiral_order.append(matrix[bottom_row][right_col])
                else:
                    for col in range(right_col, left_col, -1):
                        spiral_order.append(matrix[bottom_row][col])

            # Left column (bottom to top)
            if left_col != right_col:
                for row in range(bottom_row, top_row, -1):
                    spiral_order.append(matrix[row][left_col])

            row_st += 1
            col_st += 1

        return spiral_order


matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
]


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12],
#     [13, 14, 15],
#     [16, 17, 18],
#     [19, 20, 21],
#     [22, 23, 24],
# ]
print(Solution().spiralOrder(matrix))
