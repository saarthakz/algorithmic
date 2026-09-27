"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.
"""

from typing import List
import bisect


class Solution:
    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:

        if len(intervals) == 0:
            return [new_interval]

        insertion_idx = bisect.bisect_left(intervals, new_interval)

        # Insertion at the last place
        if insertion_idx == len(intervals):
            if intervals[insertion_idx - 1][1] < new_interval[0]:
                intervals.append(new_interval)
            else:
                intervals[insertion_idx - 1][1] = max(
                    intervals[insertion_idx - 1][1],
                    new_interval[1],
                )
            return intervals

        # Insertion at first place, check if the existing start is greater than new_interval end
        if insertion_idx == 0:
            intervals.insert(0, new_interval)

        # Insertion in between
        # Check if the start of the new interval overlaps with the previous element end
        elif new_interval[0] > intervals[insertion_idx - 1][1]:
            # New interval inserted in between, merging will commence next
            intervals.insert(insertion_idx, new_interval)

        else:
            # New interval merged with the previous element directly, merging will commence next
            intervals[insertion_idx - 1][1] = new_interval[1]
            insertion_idx -= 1

        while (
            insertion_idx < len(intervals) - 1
            and intervals[insertion_idx][1] >= intervals[insertion_idx + 1][0]
        ):
            removed_interval = intervals.pop(insertion_idx + 1)
            intervals[insertion_idx][1] = max(
                intervals[insertion_idx][1],
                removed_interval[1],
            )

        return intervals
