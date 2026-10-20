"""
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.
"""

from typing import List, Dict, Tuple


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        return self.helper(nums, memo, 0, 0, 0)

    def helper(
        self,
        nums: List[int],
        memo: Dict[Tuple[int, int, int], bool],
        one_sum: int,
        two_sum: int,
        idx: int,
    ):
        if idx >= len(nums):
            return one_sum == two_sum

        key = (idx, one_sum, two_sum)

        if key in memo:
            return memo[key]

        memo[key] = self.helper(
            nums,
            memo,
            one_sum + nums[idx],
            two_sum,
            idx + 1,
        ) or self.helper(
            nums,
            memo,
            one_sum,
            two_sum + nums[idx],
            idx + 1,
        )

        return memo[key]
