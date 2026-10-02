"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.
"""

from typing import List, Tuple
import heapq


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0

        def sort_key(interval: Interval):
            return interval.start

        intervals = sorted(intervals, key=sort_key)

        max_rooms = 1

        # Heap maintaining the end times of the intervals
        heap = [intervals[0].end]

        for idx in range(1, len(intervals)):
            current_interval = intervals[idx]
            heap_end_min = heap[0]

            if current_interval.start >= heap_end_min:
                heapq.heappop(heap)

            # Always push the interval's end time
            heapq.heappush(heap, current_interval.end)
            max_rooms = max(max_rooms, len(heap))

        return max_rooms
