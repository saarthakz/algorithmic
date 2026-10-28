"""
You are given two strings first and second, each consisting of lowercase English letters.

You are allowed to perform three operations on first an unlimited number of times:

    Insert a character at any position
    Delete a character at any position
    Replace a character at any position

Return the minimum number of operations to make first equal second.
"""

from typing import Dict, Tuple


class Solution:
    def minDistance(self, first: str, second: str) -> int:
        memo = {}
        return self.helper(first, second, 0, 0, memo)

    def helper(
        self,
        first: str,
        second: str,
        first_idx: int,
        second_idx: int,
        memo: Dict[Tuple[int, int], int],
    ) -> int:
        # first is exhausted, insert all remaining characters of second
        if first_idx == len(first):
            return len(second) - second_idx

        # second is exhausted, delete all remaining characters of first
        if second_idx == len(second):
            return len(first) - first_idx

        key = (first_idx, second_idx)
        if key in memo:
            return memo[key]

        # If characters already match, advance both pointers with zero extra cost
        if first[first_idx] == second[second_idx]:
            res = self.helper(first, second, first_idx + 1, second_idx + 1, memo)
        else:
            # 1 + minimum cost among the three operations
            replace_op = self.helper(first, second, first_idx + 1, second_idx + 1, memo)
            delete_op = self.helper(first, second, first_idx + 1, second_idx, memo)
            insert_op = self.helper(first, second, first_idx, second_idx + 1, memo)

            res = 1 + min(replace_op, delete_op, insert_op)

        memo[key] = res
        return res
