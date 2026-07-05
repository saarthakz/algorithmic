class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        left = 0
        seen = set()
        maxLength = 0

        for right in range(len(st)):
            while st[right] in seen:
                seen.remove(st[left])
                left += 1
            seen.add(st[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength
