"""
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
"""

from typing import List, Dict


class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        memo = {}
        return min(
            self.helper(costs, memo, 0),
            self.helper(costs, memo, 1),
        )

    def helper(self, costs: List[int], memo: Dict[int, int], idx: int) -> int:
        if idx >= len(costs):
            return 0

        if idx in memo:
            return memo[idx]

        memo[idx] = costs[idx] + min(
            self.helper(costs, memo, idx + 1),
            self.helper(costs, memo, idx + 2),
        )

        return memo[idx]
