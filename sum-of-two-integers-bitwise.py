"Given two integers a and b, return the sum of the two integers without using the + and - operators."


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            sum_ = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK

            a = sum_
            b = carry

        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)
