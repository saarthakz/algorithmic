"""
You are given a string s consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Find the [first_index, last_index] range for each character
        intervals_map = {}
        for idx, char in enumerate(s):
            if char not in intervals_map:
                intervals_map[char] = [idx, idx]
            else:
                intervals_map[char][1] = idx

        # Extract intervals and sort them by start index
        intervals = sorted(intervals_map.values(), key=lambda x: x[0])

        # Merge overlapping intervals
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Compute the length of each merged interval
        return [end - start + 1 for start, end in merged]
