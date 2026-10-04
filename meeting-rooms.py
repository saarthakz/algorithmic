"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts. The intervals may be provided in any order.

Note: (0,8),(8,10) is not considered a conflict at 8
"""

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def sort_key(interval: Interval):
            return interval.end

        # Sort meetings by end times to check chronological ordering
        intervals = sorted(intervals, key=sort_key)

        prev_end = float("-inf")
        # If any meeting starts before the prior meeting completes, there is a conflict
        for interval in intervals:
            if interval.start < prev_end:
                return False
            prev_end = interval.end

        return True
