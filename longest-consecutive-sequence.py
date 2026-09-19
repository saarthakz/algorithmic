"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = [0, 0]  # [countAhead, visited]

        def visit(num):
            """Returns the total count starting from num"""
            if num not in dic:
                return 0

            countAhead, visited = dic[num]

            if visited:
                # Already processed, return stored value + 1 (for this number)
                return countAhead + 1

            # Recursively get count from next number
            aheadCount = visit(num + 1)

            # Mark as visited and store how many numbers come after this
            dic[num] = [aheadCount, 1]

            # Return total count including this number
            return aheadCount + 1

        maxCount = 0
        for num in nums:
            if dic[num][1] == 0:  # If not visited
                maxCount = max(maxCount, visit(num))

        return maxCount
