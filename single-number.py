"""
You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with O(n) runtime complexity and use only O(1) extra space
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = nums[0]

        for idx in range(1, len(nums)):
            curr ^= nums[idx]

        return curr
