"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # forProds[i] stores product of elements to the left of index i
        forProds = [-25] * length
        forMul = nums[0]

        # backProds accumulates products from the right
        backProds = [-25] * length
        backMul = nums[length - 1]

        # Calculate prefix products and reversed suffix products
        for idx in range(1, len(nums)):
            forProds[idx] = forMul
            backProds[idx] = backMul
            forMul *= nums[idx]
            backMul *= nums[length - 1 - idx]

        # Reverse backProds so backProds[i] corresponds to the suffix product for index i
        backProds = list(reversed(backProds))

        ans = [-25] * length

        # Multiply prefix and suffix products for each index
        for idx in range(length):
            forw = forProds[idx]
            back = backProds[idx]

            # Use 1 for boundary elements where prefix or suffix does not exist
            if forw == -25:
                forw = 1
            if back == -25:
                back = 1

            ans[idx] = forw * back

        return ans
