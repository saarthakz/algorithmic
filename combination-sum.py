from typing import List


class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_list = set()
        nums = sorted(nums)
        self.combinationSumHelper(nums, [], target, ans_list)
        return list(list(tp) for tp in ans_list)

    def combinationSumHelper(
        self,
        nums: List[int],
        curr_combo: List[int],
        target: int,
        ans_list: set[tuple[int, ...]],
    ) -> None:


        # Base case if the target is 0
        if target == 0:
            ans_list.add(tuple(curr_combo))
            return

        # Base cae if empty list of numbers received
        if not len(nums):
            return

        # Base case to stop infinite recursion
        # Assuming nums is always a sorted array, if the smallest element is greater than target, we can not go further on this branch
        if len(nums) >= 1 and nums[0] > target:
            return

        # Now comes the real problem splitting

        # Consider and reuse the element
        self.combinationSumHelper(
            nums,
            [*curr_combo, nums[0]],
            target - nums[0],
            ans_list,
        )

        # Consider and do not reuse the element
        self.combinationSumHelper(
            nums[1:],
            [*curr_combo, nums[0]],
            target - nums[0],
            ans_list,
        )

        # Do not consider and do not reuse
        self.combinationSumHelper(
            nums[1:],
            curr_combo,
            target,
            ans_list,
        )

        return
