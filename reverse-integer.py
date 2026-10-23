"""
You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.
"""


class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits: [-2^31, 2^31 - 1]
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        # Track the sign of the input
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        while x:
            # Extract the last digit
            mod = x % 10

            # Append the digit to the reversed result
            res = res * 10 + mod

            # Remove the last digit from x
            x //= 10

        # Restore original sign
        res *= sign

        # Check for 32-bit signed integer overflow
        # Mirrors the C++ intent of returning 0 on overflow
        if res < INT_MIN or res > INT_MAX:
            return 0

        return res
