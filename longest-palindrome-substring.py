"""
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.
"""


class Solution:
    def longestPalindrome(self, st: str) -> str:

        if len(st) == 1:
            return st

        max_length = 0
        max_length_range = (-1, -1)

        # Checking for single character start points
        for idx, char in enumerate(st):
            left, right = self.expand_around(st=st, left=idx, right=idx)
            length = right - left + 1
            if length > max_length:
                max_length = length
                max_length_range = (left, right)

        for idx in range(len(st) - 1):
            first = st[idx]
            second = st[idx + 1]
            if first == second:
                left, right = self.expand_around(st=st, left=idx, right=idx + 1)
                length = right - left + 1
                if length > max_length:
                    max_length = length
                    max_length_range = (left, right)

        return st[max_length_range[0] : max_length_range[1] + 1]

    def expand_around(self, st: str, left: int, right: int):
        while (left > 0) and (right < len(st) - 1) and st[left - 1] == st[right + 1]:

            left = left - 1
            right = right + 1

        return (left, right)
