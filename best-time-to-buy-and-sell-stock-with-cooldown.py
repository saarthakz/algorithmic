"""
You are given an integer array prices where prices[i] is the price of Coin on the ith day.

You may buy and sell one Coin multiple times with the following restrictions:

    After you sell your Coin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
    You may only own at most one Coin at a time.

You may complete as many transactions as you like.

Return the maximum profit you can achieve.
"""

from typing import List, Tuple, Dict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo: Dict[Tuple[int, bool], int] = {}
        return self.helper(prices, 0, False, memo)

    def helper(
        self,
        prices: List[int],
        idx: int,
        holding: bool,
        memo: Dict[Tuple[int, bool], int],
    ) -> int:

        if idx >= len(prices):
            return 0

        key = (idx, holding)

        if key in memo:
            return memo[key]

        # Skip today regardless of holding status
        skip = self.helper(prices, idx + 1, holding, memo)

        if holding:
            # Sell today; cooldown requires skipping the next day
            sell = prices[idx] + self.helper(prices, idx + 2, False, memo)
            memo[key] = max(skip, sell)
        else:
            # Buy today
            buy = -prices[idx] + self.helper(prices, idx + 1, True, memo)
            memo[key] = max(skip, buy)

        return memo[key]
