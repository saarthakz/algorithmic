"""
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.
"""

from typing import List, Set, Tuple


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
