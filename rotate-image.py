"""
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        assert len(matrix) == len(matrix[0]), "Not a square matrix"

        dim = len(matrix)

        for idx in range(dim // 2):

            # Rotating
            for _idx in range(idx, dim - 1 - idx):

                # idx, _idx -> _idx, dim - 1 - idx
                # _idx, dim - 1 - idx -> dim - 1 - idx, dim - 1 - _idx
                # dim - 1 - idx, dim - 1 - _idx -> dim - 1 - _idx, idx
                # dim - 1 - _idx, idx -> idx, _idx

                temp = matrix[_idx][dim - 1 - idx]
                matrix[_idx][dim - 1 - idx] = matrix[idx][_idx]
                matrix[dim - 1 - idx][dim - 1 - _idx], temp = (
                    temp,
                    matrix[dim - 1 - idx][dim - 1 - _idx],
                )
                matrix[dim - 1 - _idx][idx], temp = temp, matrix[dim - 1 - _idx][idx]
                matrix[idx][_idx] = temp
