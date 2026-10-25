"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.
"""

from typing import List, Dict, Tuple


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        return self.helper(amount, coins, 0, memo)

    def helper(
        self, amount: int, coins: List[int], idx: int, memo: Dict[Tuple[int, int], int]
    ):
        # Target reached
        if amount == 0:
            return 1

        # Unreachable target
        if amount < 0 or idx >= len(coins):
            return 0

        key = (idx, amount)

        if key in memo:
            return memo[key]

        # Target yet to reach
        memo[key] = self.helper(amount - coins[idx], coins, idx, memo) + self.helper(
            amount, coins, idx + 1, memo
        )

        return memo[key]
