"""
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points are returned.)
"""

from typing import List, Tuple
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap: List[Tuple[int, List[int]]] = []

        for x, y in points:
            distance = (x**2) + (y**2)
            dist_point = (distance, [x, y])
            heapq.heappush(min_heap, dist_point)

        ans = []
        while k:
            ans.append(heapq.heappop(min_heap)[1])
            k -= 1
        return ans
