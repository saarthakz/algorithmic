"""
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        arr = []
        # Extract bits from least to most significant
        while n:
            arr.append(n % 2)
            n = n // 2

        # Pad zeroes to complete 32 bits
        trailing_cnt = 32 - len(arr)
        arr.extend([0] * trailing_cnt)

        # Reconstruct integer from the reversed 32-bit array
        n = 0
        for idx, bit in enumerate(reversed(arr)):
            n += bit * (2**idx)

        return n
