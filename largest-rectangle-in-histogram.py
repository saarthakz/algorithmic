"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for idx, height in enumerate(heights):
            start = idx

            # Pop while the top of the height stack is greater than current height
            while stack and stack[-1][1] > height:
                pop_idx, pop_height = stack.pop()
                width = idx - pop_idx
                max_area = max(max_area, pop_height * width)
                start = pop_idx
            stack.append((start, height))
        return max_area
