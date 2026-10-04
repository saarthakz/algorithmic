"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Pointer to buy day (lowest buying price seen)
        right = 1  # Pointer to sell day
        maxProfit = 0

        while right < len(prices):
            # If profitable trade, update maximum profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            # If price dropped below our buying price, reset buy pointer to current day
            else:
                left = right
            right += 1

        return maxProfit
