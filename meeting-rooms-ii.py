"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.
"""

from typing import List, Tuple

# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end


# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:

#         def sort_key(interval: Interval):
#             return interval.end

#         intervals = sorted(intervals, key=sort_key)

#         ctr = 0
#         prev_end = float("-inf")
#         while len(intervals) > 1:
#             ctr += 1
#             print(len(intervals))
#             next_list: List[Interval] = []
#             for interval in intervals:
#                 if interval.start < prev_end:
#                     next_list.append(interval)
#                 else:
#                     prev_end = interval.end
#             intervals = next_list

#         return ctr + len(intervals)


class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> int:

        def sort_key(interval: Tuple[int, int]):
            return interval[1]

        intervals = sorted(intervals, key=sort_key)

        print(intervals)

        ctr = 0
        while len(intervals) > 1:
            prev_end = float("-inf")
            ctr += 1
            print(intervals)
            next_list: List[Tuple[int, int]] = []
            for interval in intervals:
                if interval[0] < prev_end:
                    next_list.append(interval)
                else:
                    prev_end = interval[1]
            intervals = next_list

        return ctr + len(intervals)


interval_times = [(0, 40), (5, 10), (15, 20)]
interval_times = [(1, 5), (5, 10), (10, 15), (15, 20)]
interval_times = [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)]

interval_times = [
    (25, 579),
    (218, 918),
    (1281, 1307),
    (623, 1320),
    (685, 1353),
    (1308, 1358),
]

# def interval_conv_fn(interval: Tuple[int, int]):
#     return Interval(interval[0], interval[1])


# intervals = list(map(interval_conv_fn, interval_times))


print(Solution().minMeetingRooms(interval_times))
