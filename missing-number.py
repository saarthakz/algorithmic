"""
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        expected_sum = (n * (n + 1)) // 2

        return expected_sum - num_sum
