"""
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.
"""

from typing import List, Tuple, Set


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.set_of_ss: Set[Tuple[int, ...]] = set()
        curr_ss = []
        self.helper(nums, curr_ss, 0)

        ans = [list(ss) for ss in self.set_of_ss]
        return ans

    def helper(self, nums: List[int], curr_ss: List[int], idx: int):
        if idx == len(nums):
            return

        self.set_of_ss.add(tuple(curr_ss))

        # Skipping the current number for the subset
        self.helper(nums, curr_ss, idx + 1)

        # Selecting the current number for the subset
        curr_ss.append(nums[idx])
        self.set_of_ss.add(tuple(curr_ss))
        self.helper(nums, curr_ss, idx + 1)
        curr_ss.pop()
