"""
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every other integer appears at most once.

Return the repeated integer.
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # In this question, length of the array is N + 1 and the values are always in [0, N] which means any value is also a valid index and this question specifically exploits that

        slow_ptr = 0
        fast_ptr = 0

        # Detect the cycle at any point
        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]

            if slow_ptr == fast_ptr:
                break

        # Detect the entry point
        slow_ptr = nums[0]

        while slow_ptr != fast_ptr:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[fast_ptr]

        return slow_ptr
