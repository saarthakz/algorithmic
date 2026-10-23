"""
Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

You may not use any built-in library functions.
"""

import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        if n < 0:
            x = 1 / x
            n = -1 * n
        while n:
            base = 1
            curr = x
            while base * 2 <= n:
                curr *= curr
                base *= 2
            n = n - base
            ans *= curr

        return ans


Solution().myPow(2, -3)


print(2**-3)
