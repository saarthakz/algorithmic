"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the total amount of water that can be trapped between the bars.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Phase 1: Extract all valley geometries using the monotonic stack
        valleys = self.extract_valleys_with_stack(height)

        # Phase 2: Compute trapped water across the recorded valley intervals
        return self.calculate_water_from_layers(height, valleys)

    def extract_valleys_with_stack(
        self,
        height: List[int],
    ) -> List[tuple[int, int, int]]:
        stack = []
        valley_layers = []  # Stores (left_wall_idx, right_wall_idx, floor_height)

        for idx, h in enumerate(height):
            # Monotonic decreasing stack: pop whenever we encounter a taller right wall
            while stack and h > height[stack[-1]]:
                mid = stack.pop()

                # If stack is empty, there is no left wall to contain the water
                if not stack:
                    break

                left = stack[-1]
                floor_level = height[mid]

                # Record the bounded horizontal slice of the valley
                valley_layers.append((left, idx, floor_level))

            stack.append(idx)

        return valley_layers

    def calculate_water_from_layers(
        self,
        height: List[int],
        valley_layers: List[tuple[int, int, int]],
    ) -> int:
        total_water = 0

        for left, right, floor_level in valley_layers:
            width = right - left - 1
            water_level = min(height[left], height[right])
            layer_height = water_level - floor_level

            total_water += width * layer_height

        return total_water
