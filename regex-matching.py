"""
You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

Return true if the pattern matches the entire input string, otherwise return false.

    '.' Matches any single character
    '*' Matches zero or more of the preceding element.

"""

from typing import Dict, Tuple


class Solution:
    def isMatch(self, st: str, pattern: str) -> bool:
        mp = {}
        return self.helper(st, pattern, 0, 0, mp)

    def helper(
        self,
        st: str,
        pattern: str,
        st_idx: int,
        pattern_idx: int,
        mp: Dict[Tuple[int, int], bool],
    ):

        # Both of bounds means both were matched
        if st_idx >= len(st) and pattern_idx >= len(pattern):
            return True

        key = (pattern_idx, st_idx)

        if key in mp:
            return mp[key]

        # Next character is *, 0 or more occurences of the current character
        if pattern_idx < len(pattern) - 1 and pattern[pattern_idx + 1] == "*":
            char = pattern[pattern_idx]

            if char == "." and pattern_idx == len(pattern) - 2:
                return True

            # Zero occurence,
            flag = self.helper(st, pattern, st_idx, pattern_idx + 2, mp)

            # One or more occurence matching
            while st_idx < len(st):

                # For "." no matching required
                if char != "." and st[st_idx] != char:
                    break
                flag = flag or self.helper(st, pattern, st_idx + 1, pattern_idx + 2, mp)
                st_idx += 1

            mp[key] = flag
            return flag

        if (
            pattern_idx < len(pattern)
            and st_idx < len(st)
            and (pattern[pattern_idx] == "." or pattern[pattern_idx] == st[st_idx])
        ):
            mp[key] = self.helper(st, pattern, st_idx + 1, pattern_idx + 1, mp)
            return mp[key]

        return False
