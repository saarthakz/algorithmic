"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
"""

from typing import List, Dict


class Solution:

    def rob(self, nums: List[int]):
        mem_map = {}
        idx = 0
        return self.rob_helper(nums, idx, mem_map)

    def rob_helper(self, nums: List[int], idx: int, mem_map: Dict[int, int]) -> int:

        if idx >= len(nums):
            return 0

        if idx == (len(nums) - 1):
            return nums[idx]

        if idx in mem_map:
            return mem_map[idx]

        # Two options
        # Option 1, rob current and get rid of the neighbour
        opt_one = nums[idx] + self.rob_helper(nums, idx + 2, mem_map)

        # Option 2, ignore the current one, start investigating from next
        opt_two = self.rob_helper(nums, idx + 1, mem_map)

        mem_map[idx] = max(opt_one, opt_two)
        return mem_map[idx]
