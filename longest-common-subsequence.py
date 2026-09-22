"""
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

    For example, "cat" is a subsequence of "crabt".

A common subsequence of two strings is a subsequence that exists in both strings.
"""

from typing import Dict, Tuple


class Solution:
    def longestCommonSubsequence(self, first: str, second: str) -> int:
        mp: Dict[Tuple[int, int], int] = {}
        return self.helper(first, second, 0, 0, mp)

    def helper(
        self,
        first: str,
        second: str,
        first_idx: int,
        second_idx: int,
        mp: Dict[Tuple[int, int], int],
    ) -> int:

        # Indices out of bounds
        if first_idx == len(first) or second_idx == len(second):
            return 0

        if (first_idx, second_idx) in mp:
            return mp[(first_idx, second_idx)]
        ans = 0

        # Common element found
        if first[first_idx] == second[second_idx]:
            ans = 1 + self.helper(first, second, first_idx + 1, second_idx + 1, mp)
        else:
            ans = max(
                self.helper(
                    first,
                    second,
                    first_idx + 1,
                    second_idx,
                    mp,
                ),
                self.helper(
                    first,
                    second,
                    first_idx,
                    second_idx + 1,
                    mp,
                ),
            )
        mp[(first_idx, second_idx)] = ans
        return ans
