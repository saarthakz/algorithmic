"""
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        # Expected arithmetic sum of numbers from 0 to n: n * (n + 1) // 2
        expected_sum = (n * (n + 1)) // 2

        # Difference between expected sum and actual sum is the missing number
        return expected_sum - num_sum
