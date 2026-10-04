"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array to enable binary search lookup and easy triplet ordering
        nums = sorted(nums)

        ansSet = set()
        ans = []

        # Standard binary search helper to locate complement
        def binarySearch(nums: List[int], target: int, left: int, right: int):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return binarySearch(nums, target, mid + 1, right)
            else:
                return binarySearch(nums, target, left, mid - 1)

        # Fix the first element, iterate through second element, and binary search for third
        for idx, num in enumerate(nums):
            targetSum = -num

            for _idx in range(idx + 1, len(nums)):
                firstNum = nums[_idx]
                secondNum = targetSum - firstNum

                # Search for required complement in remaining elements
                secondNumIdx = binarySearch(nums, secondNum, _idx + 1, len(nums) - 1)
                if secondNumIdx != -1:
                    ansSet.add("_".join([str(num), str(firstNum), str(secondNum)]))

        # Convert serialized unique triplets back into integer lists
        for st in ansSet:
            ans.append([int(x) for x in st.split("_")])

        return ans
