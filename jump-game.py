"""
You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        can_jump_marker = [0] * len(nums)

        idx = len(nums) - 1
        while idx >= 0:
            required_jump = len(nums) - 1 - idx

            # Can directly jump, mark True and continue the backward walk
            if nums[idx] >= required_jump:
                can_jump_marker[idx] = 1

            # Can not directly jump, let's see if a jump to another tile is possible, which would make that final jump
            else:
                for _idx in range(idx + 1, idx + nums[idx] + 1):
                    if can_jump_marker[_idx]:
                        can_jump_marker[idx] = 1
                        break
            idx -= 1

        return can_jump_marker[0] == 1
