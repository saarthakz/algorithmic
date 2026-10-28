"""
You are given two strings "first" and "second", both consisting of english letters.

Return the number of distinct subsequences of "first" which are equal to "second".
"""

from typing import Dict, Tuple


class Solution:
    def numDistinct(self, first: str, second: str) -> int:
        mp = {}
        return self.helper(first, 0, second, 0, mp)

    def helper(
        self,
        first: str,
        first_idx: int,
        second: str,
        second_idx: int,
        mp: Dict[Tuple[int, int], int],
    ):
        # Out of bounds
        if second_idx >= len(second) or first_idx >= len(first):
            return 0

        key = (first_idx, second_idx)

        if key in mp:
            return mp[key]

        # Regardless of match found or not, skip to the next index in first
        skip = self.helper(first, first_idx + 1, second, second_idx, mp)

        if not first[first_idx] == second[second_idx]:
            mp[key] = skip
            return skip

        if second_idx == len(second) - 1:
            match = 1
        else:
            match = self.helper(first, first_idx + 1, second, second_idx + 1, mp)

        mp[key] = skip + match

        return skip + match
