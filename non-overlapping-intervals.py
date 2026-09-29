"""
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.
"""

from bisect import bisect_left
from typing import List

"""
The recursive approach runs into stack overflow problem
"""

# class Solution:

#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0

#         # 1. Sort primarily by start times
#         intervals.sort(key=lambda x: x[0])
#         n = len(intervals)

#         # 2. Extract start times to enable O(log n) next-compatible lookups
#         start_times = [interval[0] for interval in intervals]

#         # 3. Initialize memoization table with sentinel -1 values
#         memo = [-1] * n

#         # 4. Find max compatible intervals retained, then compute removals
#         max_kept = self.helper(0, intervals, start_times, memo)
#         return n - max_kept

#     def helper(
#         self,
#         idx: int,
#         intervals: List[List[int]],
#         start_times: List[int],
#         memo: List[int],
#     ) -> int:
#         """
#         Pure recursive function returning the maximum number of non-overlapping
#         intervals that can be retained from intervals[idx:].
#         """
#         # Base case: reached beyond the end of the intervals list
#         if idx >= len(intervals):
#             return 0

#         # Return cached result if already computed
#         if memo[idx] != -1:
#             return memo[idx]

#         # Choice 1: Skip the current interval
#         skip = self.helper(idx + 1, intervals, start_times, memo)

#         # Choice 2: Take the current interval
#         # Binary search for the first interval starting at or after intervals[idx][1]
#         next_idx = bisect_left(start_times, intervals[idx][1])
#         take = 1 + self.helper(next_idx, intervals, start_times, memo)

#         # Record in memo and return
#         memo[idx] = max(skip, take)
#         return memo[idx]


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 1. Sort by start times
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        start_times = [interval[0] for interval in intervals]

        # dp[i] stores the max non-overlapping intervals kept from intervals[i:]
        # Size n + 1 so dp[n] = 0 acts as the base case
        dp = [0] * (n + 1)

        # 2. Fill iteratively from back to front
        for i in range(n - 1, -1, -1):
            # Option 1: Skip interval i
            skip = dp[i + 1]

            # Option 2: Take interval i and jump to next compatible interval
            next_idx = bisect_left(start_times, intervals[i][1])
            take = 1 + dp[next_idx]

            dp[i] = max(skip, take)

        # Minimum removals = total intervals - maximum kept
        return n - dp[0]
