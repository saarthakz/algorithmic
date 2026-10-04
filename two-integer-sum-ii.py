"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.
"""

from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right and right >= 0:
            curr = numbers[left] + numbers[right]

            if curr == target:
                return [left + 1, right + 1]

            if curr > target:
                right = right - 1
            else:
                left = left + 1

        return [0, 0]
