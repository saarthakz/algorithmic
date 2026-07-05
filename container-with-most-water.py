from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left <= right:

            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            if area > maxArea:
                maxArea = area

            if heights[left] == height:
                left += 1
            else:
                right -= 1

        return maxArea
