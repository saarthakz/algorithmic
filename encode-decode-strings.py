"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return "---"
        return "#*#".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "---":
            return []
        return s.split("#*#")
