from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ansSet = set()
        ans = []

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

        for idx, num in enumerate(nums):
            targetSum = -num

            for _idx in range(idx + 1, len(nums)):
                firstNum = nums[_idx]
                secondNum = targetSum - firstNum

                secondNumIdx = binarySearch(nums, secondNum, _idx + 1, len(nums) - 1)
                if secondNumIdx != -1:
                    ansSet.add("_".join([str(num), str(firstNum), str(secondNum)]))

        for st in ansSet:
            ans.append([int(x) for x in st.split("_")])

        return ans
