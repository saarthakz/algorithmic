"""
You are given two strings s1 and s2.

Return true if "second_str" contains a permutation of first_str, or false otherwise. That means if a permutation of "first_str" exists as a substring of "second_str", then return true.

Both strings only contain lowercase letters.
"""

from typing import Dict
from collections import Counter
from copy import deepcopy


class Solution:
    def checkInclusion(self, first_str: str, second_str: str) -> bool:
        ref_ctr = Counter(first_str)
        copy_ctr = deepcopy(ref_ctr)
        in_window = False
        start = 0

        for idx, char in enumerate(second_str):

            # Found a character of interest
            if char in copy_ctr:

                # Mark the window flag as True and set the 'start' pointer
                if not in_window:
                    in_window = True
                    start = idx

                copy_ctr[char] -= 1

                # If the entire counter is zeroed, we have successfully found a permutation
                if self.is_ctr_zeroed(copy_ctr):
                    return True

                # We need to shrink the window and move the 'start' pointer
                if copy_ctr[char] < 0:
                    while copy_ctr[char] < 0:
                        start_char = second_str[start]
                        # Since we are in the window, all the characters exist in the copy counter
                        copy_ctr[second_str[start]] += 1
                        start += 1

                continue

            # Not a character of interest

            # If we were in the window, we need to reset it
            if in_window:
                in_window = False
                copy_ctr = deepcopy(ref_ctr)

        return False

    def is_ctr_zeroed(self, ctr: Counter[str]):
        for key in ctr.keys():
            if ctr[key] != 0:
                return False
        return True
