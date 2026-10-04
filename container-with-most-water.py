"""
You are given an integer array heights where heights[i] represents the height of the ithith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
15
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxArea = 0

        # Narrow the window from both ends, calculating area at each step
        while left <= right:
            width = right - left
            # Container height is constrained by the shorter bar
            bottleneck_height = min(heights[left], heights[right])
            area = width * bottleneck_height

            if area > maxArea:
                maxArea = area

            # Move the pointer with the shorter bar inward to seek a taller boundary
            if heights[left] == bottleneck_height:
                left += 1
            else:
                right -= 1

        return maxArea
