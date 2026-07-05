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
