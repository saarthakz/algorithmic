"""
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.
"""

from typing import List, Deque
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter_mapping = {
            2: {"a", "b", "c"},
            3: {"d", "e", "f"},
            4: {"g", "h", "i"},
            5: {"j", "k", "l"},
            6: {"m", "n", "o"},
            7: {"p", "q", "r", "s"},
            8: {"t", "u", "v"},
            9: {"w", "x", "y", "z"},
        }

        queue: Deque[str] = deque([""])
        ans = []

        if len(digits) == 0:
            return []

        while len(queue):
            curr = queue.popleft()

            if len(curr) == len(digits):
                ans.append(curr)
                continue

            next_digit = int(digits[len(curr)])

            for next_char in digit_letter_mapping[next_digit]:
                queue.append(f"{curr}{next_char}")

        return ans
