"""
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.
"""


class Solution:
    def countSubstrings(self, st: str) -> int:

        if len(st) == 1:
            return 1

        total_cnt = 0

        # Checking for single character start points
        for idx, char in enumerate(st):
            total_cnt += self.expand_around_and_count(
                st=st,
                left=idx,
                right=idx,
            )

        for idx in range(len(st) - 1):
            first = st[idx]
            second = st[idx + 1]
            if first == second:
                total_cnt += self.expand_around_and_count(
                    st=st,
                    left=idx,
                    right=idx + 1,
                )

        return total_cnt

    def expand_around_and_count(
        self,
        st: str,
        left: int,
        right: int,
    ):
        cnt = 1
        while (left > 0) and (right < len(st) - 1) and st[left - 1] == st[right + 1]:
            left = left - 1
            right = right + 1
            cnt += 1
        return cnt
