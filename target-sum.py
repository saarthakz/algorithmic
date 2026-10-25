"""
You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

    For example, if nums = [1, 2], one possible sum would be "+1-2=-1".

If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.
"""

from typing import List, Tuple, Dict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.helper(nums, target, 0, memo)

    def helper(
        self, nums: List[int], target: int, idx: int, memo: Dict[Tuple[int, int], int]
    ):
        # Evaluation after the entire list has been processed
        if idx == len(nums) and target == 0:
            return 1

        # In other out of bound conditions, return 0
        if idx >= len(nums):
            return 0

        key = (idx, target)

        if not key in memo:
            memo[key] = self.helper(
                nums, target + nums[idx], idx + 1, memo
            ) + self.helper(nums, target - nums[idx], idx + 1, memo)

        return memo[key]
