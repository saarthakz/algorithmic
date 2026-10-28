"""
You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

To obtain target, you may apply the following operation on triplets zero or more times:

Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
* E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

Return true if it is possible to obtain target as an element of triplets, or false otherwise.
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        has_x = has_y = has_z = False

        for a, b, c in triplets:
            # Discard invalid triplets that would overshoot
            if a > x or b > y or c > z:
                continue

            # Check if this valid triplet supplies any target values
            if a == x:
                has_x = True
            if b == y:
                has_y = True
            if c == z:
                has_z = True

            # Early exit if all target components have been matched
            if has_x and has_y and has_z:
                return True

        return has_x and has_y and has_z
