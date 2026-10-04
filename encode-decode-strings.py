"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Sentinel value for empty list
        if not len(strs):
            return "---"
        # Join strings using a delimiter that separates tokens
        return "#*#".join(strs)

    def decode(self, s: str) -> List[str]:
        # Handle sentinel value for empty list
        if s == "---":
            return []
        # Split on the delimiter to recover original strings
        return s.split("#*#")
