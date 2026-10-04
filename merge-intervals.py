"""
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals by start time to bring overlapping intervals adjacent to each other
        intervals = sorted(intervals)
        idx = 0

        # Iteratively merge overlapping neighbors
        while idx < len(intervals) - 1:
            self.expand_interval_if_applicable(
                idx=idx,
                intervals=intervals,
            )
            idx += 1

        return intervals

    def expand_interval_if_applicable(self, idx: int, intervals: List[List[int]]):
        # Merge next interval if it overlaps with current interval
        while idx < len(intervals) - 1 and intervals[idx][1] >= intervals[idx + 1][0]:
            removed_interval = intervals.pop(idx + 1)
            intervals[idx][1] = max(
                intervals[idx][1],
                removed_interval[1],
            )
