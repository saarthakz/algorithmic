"Given two integers a and b, return the sum of the two integers without using the + and - operators."


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        # Simulate 32-bit binary addition until no carry remains
        while b != 0:
            # XOR computes sum of bits without considering carry
            sum_ = (a ^ b) & MASK
            # AND followed by left shift computes the carry bits
            carry = ((a & b) << 1) & MASK

            a = sum_
            b = carry

        # If positive/non-negative 32-bit int, return directly; else recover negative signed value
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)
