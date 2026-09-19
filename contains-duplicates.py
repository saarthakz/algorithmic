"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
