from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Group by length
        length_groups = defaultdict(list)
        for s in strs:
            length_groups[len(s)].append(s)

        result = []

        # Step 2: Process each length group
        for length, words in length_groups.items():
            # Skip groups with 0 or 1 strings
            if len(words) <= 1:
                result.append(words)
                continue

            # Use frequency map as hash key
            anagram_map = defaultdict(list)
            for word in words:
                # Create frequency map as a tuple (hashable)
                freq = [0] * 26
                for char in word:
                    freq[ord(char) - ord("a")] += 1

                # Use tuple of frequencies as key
                key = tuple(freq)
                anagram_map[key].append(word)

            # Add all anagram groups to result
            result.extend(anagram_map.values())

        return result
