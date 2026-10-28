"""
You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

    |n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

You may assume that s1, s2 and s3 consist of lowercase English letters.
"""

from typing import Dict, Tuple


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) == 0:
            return s2 == s3

        if len(s2) == 0:
            return s1 == s3

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        return self.helper(s1, s2, s3, 0, 0, 0, memo)

    def helper(
        self,
        first: str,
        second: str,
        result: str,
        first_idx: int,
        second_idx: int,
        res_idx: int,
        memo: Dict[Tuple[int, int], bool],
    ):
        # Base case
        # At the last character of result
        # This implies
        if res_idx == len(result) - 1:
            # That either second string is complete and first is at it's last index or
            if first_idx == len(first) - 1 and first[first_idx] == result[res_idx]:
                return True
            # That either first string is complete and second is at it's last index
            elif (
                second_idx == len(second) - 1 and second[second_idx] == result[res_idx]
            ):
                return True
            else:
                return False

        key = (first_idx, second_idx)
        if key in memo:
            return memo[key]

        first_res = second_res = False

        if first_idx < len(first) and first[first_idx] == result[res_idx]:
            first_res = self.helper(
                first, second, result, first_idx + 1, second_idx, res_idx + 1, memo
            )

        if second_idx < len(second) and second[second_idx] == result[res_idx]:
            second_res = self.helper(
                first, second, result, first_idx, second_idx + 1, res_idx + 1, memo
            )

        memo[key] = first_res or second_res
        return memo[key]
