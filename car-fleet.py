"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
"""

from typing import List, Tuple


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:

        # Distance
        distances = [target - pos for pos in positions]

        # Combining distance and speed together
        dist_speeds = list(zip(distances, speeds))

        def sort_key(dist_speed: Tuple[int, int]):
            # Sorting by distance
            return dist_speed[0]

        # Sort by distance
        # Reason we sort by position is because the farthest car will always be the ultimate bottleneck
        dist_speeds = sorted(dist_speeds, key=sort_key)

        # Stack of times
        st = [self.get_time(dist_speeds[0])]

        for idx in range(1, len(dist_speeds)):
            curr = dist_speeds[idx]
            curr_time = self.get_time(curr)

            if curr_time > st[-1]:
                st.append(curr_time)

        return len(st)

    def get_time(self, dist_speed: Tuple[int, int]):
        return dist_speed[0] / dist_speed[1]
