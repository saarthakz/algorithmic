"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
"""

from typing import List, Dict, Tuple


class Solution:
    INT_MAX = int(3e5)

    def coinChange(self, coins: List[int], amount: int) -> int:

        # (amount, idx) -> min_picked mapping
        mp: Dict[Tuple[int, int], int] = {}
        ans = self.helper(
            coins=coins,
            amount=amount,
            idx=0,
            mp=mp,
        )
        return -1 if ans == self.INT_MAX else ans

    def helper(
        self,
        coins: List[int],
        amount: int,
        idx: int,
        mp: Dict[Tuple[int, int], int],
    ):
        # No more amount left, hence the current combinational trail is viable
        if amount == 0:
            return 0

        # Amount remains but out of bounds
        if idx >= len(coins):
            return self.INT_MAX

        if (amount, idx) in mp:
            return mp[(amount, idx)]

        ans = self.INT_MAX

        # If current coin can be picked, try it
        if coins[idx] <= amount:
            ans = 1 + self.helper(
                coins=coins,
                amount=amount - coins[idx],
                idx=idx,
                mp=mp,
            )

        # Let's not pick the current coin and proceed
        ans = min(
            ans,
            self.helper(
                coins=coins,
                amount=amount,
                idx=idx + 1,
                mp=mp,
            ),
        )

        mp[(amount, idx)] = ans
        return ans
