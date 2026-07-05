from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while nums[left] > nums[right]:
            mid = (left + right) // 2

            if right == left + 1:
                left = right
                break

            if nums[mid] > nums[left]:
                left = mid
                continue

            if nums[mid] < nums[right]:
                right = mid
                continue

        return nums[left]
