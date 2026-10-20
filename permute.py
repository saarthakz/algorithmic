"""
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.
"""

from typing import List, Tuple, Deque, Set
from copy import deepcopy
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tracker: Deque[Tuple[List[int], Set[int]]] = deque([([], set(nums))])
        ans: List[List[int]] = []
        while len(tracker):
            curr_perm, remaining_elems = tracker.popleft()
            for elem in remaining_elems:
                curr_perm_cp = deepcopy(curr_perm)
                curr_perm_cp.append(elem)
                remaining_elems_cp = deepcopy(remaining_elems)
                remaining_elems_cp.remove(elem)

                if len(remaining_elems_cp):
                    tracker.append((curr_perm_cp, remaining_elems_cp))
                else:
                    ans.append(curr_perm_cp)

        return ans
