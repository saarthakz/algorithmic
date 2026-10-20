"""
Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.
"""

from typing import List, Set, Tuple, Dict
from bisect import bisect_left


class Solution:
    def partition(self, st: str) -> List[List[str]]:

        palindrome_range_set: Set[Tuple[int, int]] = set()

        # Checking for single character start points
        for idx, char in enumerate(st):
            palindrome_range_set.update(
                self.get_palindrome_ranges(st=st, left=idx, right=idx)
            )

        # Double character start points
        for idx in range(len(st) - 1):
            first = st[idx]
            second = st[idx + 1]
            if first == second:
                palindrome_range_set.update(
                    self.get_palindrome_ranges(st=st, left=idx, right=idx + 1)
                )

        range_mp: Dict[int, Set[int]] = {}

        for start, end in palindrome_range_set:
            range_mp.setdefault(start, set()).add(end)

        combos = [[(0, end)] for end in range_mp[0]]
        all_palindrome_range_trails: List[List[Tuple[int, int]]] = []

        while len(combos):
            # Current combo trail
            combo = combos.pop()

            # Get the last "end" of the trail
            end = combo[-1][1]

            # If the end is the string end,
            # Then we no longer need to add this trail back to the combos
            if end + 1 == len(st):
                all_palindrome_range_trails.append(combo)
                continue

            # Else, use "end" as the next palindrome range start indicator
            next_start = end + 1
            for next_end in range_mp[next_start]:
                combo_cp = combo[:]
                combo_cp.append((next_start, next_end))
                combos.append(combo_cp)

        all_ans = []

        for palindrome_range_trail in all_palindrome_range_trails:
            ans = []
            for start, end in palindrome_range_trail:
                ans.append(st[start : end + 1])
            all_ans.append(ans)

        return all_ans

    def get_palindrome_ranges(self, st: str, left: int, right: int):
        ranges: List[Tuple[int, int]] = [(left, right)]
        while (left > 0) and (right < len(st) - 1) and st[left - 1] == st[right + 1]:
            ranges.append((left, right))
            left = left - 1
            right = right + 1

        ranges.append((left, right))

        return ranges
