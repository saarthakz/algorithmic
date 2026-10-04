"""
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.
"""

from typing import List
import copy
import math


class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]

        cnt_arr = [0]
        multiplier = int(math.log2(n)) + 1

        # Progressively double array by appending previous counts incremented by 1
        for _ in range(int(multiplier)):
            self.unfold(cnt_arr)

        ans = [0] * (n + 1)

        for idx in range(n + 1):
            ans[idx] = cnt_arr[idx]

        return ans

    def unfold(self, cnt_arr: List[int]):
        # Numbers in the next power-of-two range have identical bit counts + 1 (the MSB)
        ext = [0] * len(cnt_arr)
        for idx, cnt in enumerate(cnt_arr):
            ext[idx] = 1 + cnt_arr[idx]
        cnt_arr.extend(ext)
