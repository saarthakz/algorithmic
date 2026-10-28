"""
You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

Return the maximum number of coins you can receive by bursting all of the balloons.
"""

from typing import List
from copy import deepcopy
from typing import Dict, Tuple


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        mp = {}
        return self.helper(nums, mp)

    def helper(self, nums: List[int], mp: Dict[Tuple[int, ...], int]):

        if len(nums) == 1:
            return nums[0]

        key = tuple(nums)

        if key in mp:
            return mp[key]

        max_coins = nums[0]

        for idx in range(len(nums)):
            nums_cp = deepcopy(nums)
            curr = nums[idx]
            if idx == 0:
                curr *= nums[idx + 1]
            elif idx == len(nums) - 1:
                curr *= nums[idx - 1]
            else:
                curr *= nums[idx - 1] * nums[idx + 1]

            nums_cp.pop(idx)
            max_coins = max(max_coins, curr + self.helper(nums_cp, mp))

        mp[key] = max_coins
        return max_coins
