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
