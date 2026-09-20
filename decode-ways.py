"""
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

    "JAB" with the grouping (10 1 2)
    "JL" with the grouping (10 12)

The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.
"""

from typing import Set, Dict


class Solution:
    def numDecodings(self, st: str) -> int:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digi_set: Set[str] = set()
        for char in alpha:
            ascii = ord(char) - 64
            self.digi_set.add(str(ascii))

        mp: Dict[int, int] = {}

        return self.helper(st=st, curr_idx=0, mp=mp)

    def helper(self, st: str, curr_idx: int, mp: Dict[int, int]) -> int:

        if curr_idx >= len(st):
            return 0

        if curr_idx == len(st) - 1 and st[curr_idx] != "0":
            return 1

        if st[curr_idx] == "0":
            return 0

        if curr_idx in mp:
            return mp[curr_idx]

        result = self.helper(st=st, curr_idx=curr_idx + 1, mp=mp)

        two_char_st = st[curr_idx : curr_idx + 2]
        if two_char_st in self.digi_set:
            result += (
                1
                if curr_idx + 2 == len(st)
                else self.helper(st=st, curr_idx=curr_idx + 2, mp=mp)
            )

        mp[curr_idx] = result

        return result


st = "06"

print(Solution().numDecodings(st))
