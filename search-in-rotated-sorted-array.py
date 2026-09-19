"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            if left == right and target != nums[left]:
                return -1

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if right == left + 1:
                if target == nums[left]:
                    return left
                if target == nums[right]:
                    return right
                return -1

            if nums[mid] > nums[left]:
                # mid is in the left sorted array
                if target >= nums[left] and target < nums[mid]:
                    # target is in the left sorted array
                    right = mid
                else:
                    left = mid
                continue

            if nums[mid] < nums[right]:
                # mid is in the right sorted array

                if target > nums[mid] and target <= nums[right]:
                    # target is in the right sorted array
                    left = mid
                else:
                    right = mid
