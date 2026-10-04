"""
You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

Return an array output where output[j] is the result of query[j].

Note: The length of an interval is calculated as right_i - left_i + 1.
"""

from typing import List, Dict, Tuple
import heapq


class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def sort_key(interval: List[int]):
            return interval[0]

        intervals = sorted(intervals, key=sort_key)
        min_heap: List[Tuple[int, int]] = []

        query_map: Dict[int, int] = {}

        idx = 0
        for val in sorted(set(queries)):

            # Keep on iterating from left to right in the intervals
            while idx < len(intervals) and intervals[idx][0] <= val:
                left, right = intervals[idx]
                heapq.heappush(min_heap, (right - left + 1, right))
                idx += 1

            while len(min_heap) and min_heap[0][1] < val:
                heapq.heappop(min_heap)

            query_map[val] = min_heap[0][0] if len(min_heap) else -1

        ans = [query_map[val] for val in queries]
        return ans
