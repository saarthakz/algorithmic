"""
You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:

    j <= nums[i]
    i + j < nums.length

You are initially positioned at nums[0].

Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        # We stop at len(nums) - 1 because once we reach the last index, no more jumps are needed
        for idx in range(len(nums) - 1):
            # Update the furthest point reachable from any tile visited so far
            farthest = max(farthest, idx + nums[idx])

            # When we reach the limit of our current jump
            if idx == current_end:
                jumps += 1
                current_end = farthest

                # Early exit if the boundary already covers the last index
                if current_end >= len(nums) - 1:
                    break

        return jumps
