from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = dict()
        found = False

        for idx, num in enumerate(nums):
            if num in dic:
                dic[num].append(idx)
            else:
                dic[num] = [idx]

        for idx, num in enumerate(nums):
            dicTarget = target - num
            if dicTarget in dic:
                if dicTarget != num:
                    return [idx, dic[dicTarget].pop(0)]
                elif dic[dicTarget].__len__() > 1:
                    return [idx, dic[dicTarget].pop(1)]
