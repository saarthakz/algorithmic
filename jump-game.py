"""
You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for idx in range(len(nums)):
            # If our current position is further than we could ever reach, we're stuck
            if idx > max_reach:
                return False

            # Update how far we can go: current index + jump size
            max_reach = max(max_reach, idx + nums[idx])

            # If we can reach or pass the last index, we're done!
            if max_reach >= len(nums) - 1:
                return True

        return True
