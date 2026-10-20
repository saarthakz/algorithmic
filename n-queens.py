"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.
"""

# from typing import List, Set, Tuple
# from copy import deepcopy


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         self.queen_cnt = n
#         self.rows = self.cols = n
#         self.solutions: List[Set[Tuple[int, int]]] = []

#         for col in range(self.cols):
#             self.helper(
#                 blacklist=set(),
#                 curr=(0, col),
#                 queens=set(),
#             )

#         ans = []

#         for points in self.solutions:
#             grid = [["."] * self.cols for _ in range(self.rows)]
#             for row, col in points:
#                 grid[row][col] = "Q"
#             ans_grid = ["".join(row) for row in grid]
#             ans.append(ans_grid)
#         return ans

#     def helper(
#         self,
#         blacklist: Set[Tuple[int, int]],
#         curr: Tuple[int, int],
#         queens: Set[Tuple[int, int]],
#     ):
#         if not self.in_bounds(curr):
#             return

#         if curr in blacklist:
#             return

#         row, col = curr

#         # Select the current position as a queen.
#         queens = queens.copy()
#         queens.add(curr)

#         # All queens have been placed.
#         if len(queens) == self.queen_cnt:
#             self.solutions.append(queens)
#             return

#         # Copy blacklist for this branch.
#         blacklist_cp = deepcopy(blacklist)

#         # Mark the column below the current queen.
#         for bl_row in range(row + 1, self.rows):
#             blacklist_cp.add((bl_row, col))

#         # Mark the bottom-left diagonal.
#         bl_row, bl_col = row + 1, col - 1
#         while self.in_bounds((bl_row, bl_col)):
#             blacklist_cp.add((bl_row, bl_col))
#             bl_row += 1
#             bl_col -= 1

#         # Mark the bottom-right diagonal.
#         bl_row, bl_col = row + 1, col + 1
#         while self.in_bounds((bl_row, bl_col)):
#             blacklist_cp.add((bl_row, bl_col))
#             bl_row += 1
#             bl_col += 1

#         # Explore every position in the next row.
#         next_row = row + 1
#         if next_row < self.rows:
#             for next_col in range(self.cols):
#                 self.helper(
#                     blacklist_cp,
#                     (next_row, next_col),
#                     queens,
#                 )

#     def in_bounds(self, curr: Tuple[int, int]) -> bool:
#         row, col = curr
#         return 0 <= row < self.rows and 0 <= col < self.cols


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()  # r + c
        diag2 = set()  # r - c

        board = [["."] * n for _ in range(n)]
        results: List[List[str]] = []

        def backtrack(row: int) -> None:
            if row == n:
                results.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                # Place queen and mark restrictions
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                board[row][col] = "Q"

                # Advance directly to the next row
                backtrack(row + 1)

                # Backtrack: revert state in-place (no copies needed)
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return results
