"""
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.
"""

from typing import Dict


class Solution:
    def climbStairs(self, n: int, mem_map: Dict[int, int] = {}) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 1

        if n in mem_map:
            return mem_map[n]

        # We can take either 1 step or 2 steps
        mem_map[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return mem_map[n]


print(Solution().climbStairs(38))
