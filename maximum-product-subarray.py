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

        # Ranges of all the subarrays with zeroes in it
        # Splitting the problem essentially
        # [Start, end) as in Start is inclusive but end is exclusive
        ranges: List[Tuple[int, int]] = []
        start = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                ranges.append((start, idx))
                start = idx + 1

        max_product = 0

        # Now, we operate on each "no zero" range
        for start, end in ranges:
            product = 1
            for idx in range(start, end):
                product *= nums[idx]

            # If the product of all elements in the current "no zero" range is positive
            # We can check for the max product condition early and break out
            if product > 0:
                max_product = max(max_product, product)
                break

            # Since it is negative, there is an odd count of negatives in the range,
            # Hence we need to figure out which single negative number would paritition the range to get the max partition product

            curr_product = 1
            for idx in range(start, end):
                curr_product *= nums[idx]
