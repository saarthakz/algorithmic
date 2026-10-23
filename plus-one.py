"""
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Traverse from least significant digit (right to left)
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                return digits
            digits[idx] = 0

        # If all digits were 9 (e.g., [9, 9] -> [0, 0]), prepend 1
        return [1] + digits
