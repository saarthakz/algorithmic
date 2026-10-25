"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the total amount of water that can be trapped between the bars.
"""

from typing import List, Tuple


class Solution:
    def trap(self, heights: List[int]) -> int:

        if len(heights) == 1:
            return 0

        inflection_points: List[Tuple[int, int]] = []

        # Get points of inflection (where the monotonicity changes)

        # Up direction as 1
        # Down direction as -1

        # Appending a "Zero" to the end of the list to include the actual list block in the inflection points if applicable
        heights.append(0)
        curr_dir = 1  # Start with the assumption of monotonically increasing

        for idx in range(1, len(heights)):
            # Current element is lesser than previous and the direction was set to "up"
            if heights[idx] < heights[idx - 1] and curr_dir == 1:
                inflection_points.append((idx - 1, 1))
                curr_dir = -1
                continue

            # Current element is greater than previous and the direction was set to "down"
            if heights[idx] > heights[idx - 1] and curr_dir == -1:
                inflection_points.append((idx - 1, -1))
                curr_dir = 1
                continue

        # Get all the up inflection points as these will be used as potential boundaries for trapping the water

        trap_boundaries_idx = list(
            map(
                lambda x: x[0],
                (filter(lambda x: x[1] == 1, inflection_points)),
            )
        )

        if len(trap_boundaries_idx) == 1:
            return 0

        st = [(trap_boundaries_idx[0], 1)]

        for idx in range(1, len(trap_boundaries_idx)):
            boundary_idx = trap_boundaries_idx[idx]
            boundary_height = heights[boundary_idx]

            # If stack top index height is equal to current boundary height
            if heights[st[-1][0]] == boundary_height:
                st.append((boundary_idx, st[-1][1]))
                continue

            # If stack top index height is greater than current boundary height
            if heights[st[-1][0]] > boundary_height:
                st.append((boundary_idx, -1))
                continue

            # Remaining case, the stack top index height is less than boundary height
            while len(st) and heights[st[-1][0]] < boundary_height and st[-1][1] == -1:
                st.pop()

            # Now check if the loop terminated due to direction flag or due to boundary height condition
            if boundary_height > heights[st[-1][0]]:
                st.append((boundary_idx, 1))
            else:
                st.append((boundary_idx, -1))

        total_water = 0

        for idx in range(len(st) - 1):
            left_idx = st[idx][0]
            right_idx = st[idx + 1][0]

            upper_surface = min(heights[left_idx], heights[right_idx])

            # Sum trapped water in all valleys between this boundary pair
            for col in range(left_idx + 1, right_idx):
                if upper_surface > heights[col]:
                    total_water += upper_surface - heights[col]

        return total_water
