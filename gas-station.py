"""
There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

    gas[i] is the amount of gas at the ith station.
    cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)

You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

It's guaranteed that at most one solution exists.
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        extras = [0] * len(gas)

        for idx in range(len(gas)):
            extras[idx] = gas[idx] - cost[idx]

        if sum(extras) < 0:
            return -1

        start = 0
        curr = 0

        for idx, extra in enumerate(extras):
            curr += extra
            if curr < 0:
                start = idx + 1
                curr = 0

        return start
