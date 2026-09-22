"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.
"""

from typing import List, Dict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cnt = 1
        mp: Dict[int, int] = {}

        for idx in range(len(nums)):
            cnt = max(cnt, self.helper(nums=nums, start=idx, mp=mp))

        return cnt

    def helper(self, *, nums: List[int], start: int, mp: Dict[int, int]):

        next_starts = []
        cnt = 1

        if start in mp:
            return mp[start]

        for idx in range(start, len(nums)):
            if nums[idx] > nums[start]:
                next_starts.append(idx)

        for next_start in next_starts:
            cnt = max(cnt, 1 + self.helper(nums=nums, start=next_start, mp=mp))

        mp[start] = cnt

        return cnt
