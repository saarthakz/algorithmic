"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map each value to a list of its indices to handle duplicate numbers
        dic = dict()
        found = False

        for idx, num in enumerate(nums):
            if num in dic:
                dic[num].append(idx)
            else:
                dic[num] = [idx]

        # Find the complement (target - num) for each number in the array
        for idx, num in enumerate(nums):
            dicTarget = target - num
            if dicTarget in dic:
                # If complement is a different number, return current index and first index of complement
                if dicTarget != num:
                    return [idx, dic[dicTarget].pop(0)]
                # If complement is the same number, ensure it appeared at another index
                elif dic[dicTarget].__len__() > 1:
                    return [idx, dic[dicTarget].pop(1)]
