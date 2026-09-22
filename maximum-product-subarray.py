"""
Maximum Product Subarray
Medium Topics Company Tags
Hints

Given an integer array nums, find a subarray that has the largest product, and return the product.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Note that the product of an array with a single element is the value of that element.
"""

from typing import List, Tuple


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        max_product = nums[0]

        # Ranges of all the subarrays with zeroes in it
        # Splitting the problem essentially
        # [Start, end) as in Start is inclusive but end is exclusive
        ranges: List[Tuple[int, int]] = []
        start = 0
        idx = 0

        zero_flag = False

        while idx < len(nums):
            if nums[idx] == 0:
                zero_flag = True
                ranges.append((start, idx))
                start = idx + 1
            idx += 1

        ranges.append((start, idx))

        # Now, we operate on each "no zero" range
        for start, end in ranges:
            product = 1

            # Left partitions
            for idx in range(start, end):
                product *= nums[idx]
                max_product = max(max_product, product)

            product = 1
            # Right partitions
            for idx in range(end - 1, start - 1, -1):
                product *= nums[idx]
                max_product = max(max_product, product)

        # A protection against the edge of case of zeroes and negative numbers only
        if zero_flag:
            max_product = max(max_product, 0)

        return max_product
