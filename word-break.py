"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
"""

from typing import List, Set, Dict


class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> bool:
        words_dict = set(wordDict)
        mp: Dict[int, bool] = {}
        return self.helper(st=st, words_dict=words_dict, start=0, mp=mp)

    def helper(self, st: str, words_dict: Set[str], start: int, mp: Dict[int, bool]):

        # Start out of bounds
        if start >= len(st):
            return False

        # The entire word is present in the dictionary
        if st[start:] in words_dict:
            return True

        if start in mp:
            return mp[start]

        next_starts = []
        for idx in range(start, len(st)):
            if st[start:idx] in words_dict:
                next_starts.append(idx)

        flag = False
        for next_start in next_starts:
            flag = flag or self.helper(
                st=st,
                words_dict=words_dict,
                start=next_start,
                mp=mp,
            )

        mp[start] = flag
        return flag
