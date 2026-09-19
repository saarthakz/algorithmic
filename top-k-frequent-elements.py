"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1

        sorted_nums = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)

        return sorted_nums[:k]
