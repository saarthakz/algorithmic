"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string."""


class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        left = 0
        seen = set()
        maxLength = 0

        # Sliding window: expand right pointer and shrink left when duplicates occur
        for right in range(len(st)):
            # Shrink window from the left until the duplicate character is eliminated
            while st[right] in seen:
                seen.remove(st[left])
                left += 1

            # Include current character into the window set and record max length
            seen.add(st[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength
