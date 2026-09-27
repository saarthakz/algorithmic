"""
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        arr = []
        while n:
            arr.append(n % 2)
            n = n // 2

        # Add the trailing zeroes for 32 bit
        trailing_cnt = 32 - len(arr)
        arr.extend([0] * trailing_cnt)

        n = 0
        for idx, bit in enumerate(reversed(arr)):
            n += bit * (2**idx)

        return n
