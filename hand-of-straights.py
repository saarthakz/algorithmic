"""
You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise, return false.
"""

from typing import List, Dict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()

        freq_map: Dict[int, int] = {}

        for num in hand:
            freq_map[num] = freq_map.setdefault(num, 0) + 1

        for ctr in range(len(hand) // groupSize):
            key = next(iter(freq_map))

            for _ctr in range(groupSize):
                if key not in freq_map:
                    return False
                freq_map[key] -= 1
                if freq_map[key] == 0:
                    freq_map.pop(key)
                key += 1
        return True
