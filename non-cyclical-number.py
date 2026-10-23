"""
A non-cyclical number is an integer defined by the following algorithm:

    Given a positive integer, replace it with the sum of the squares of its digits.
    Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
    If it stops at 1, then the number is a non-cyclical number.

Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.
"""

from typing import List, Set


class Solution:
    def isHappy(self, n: int) -> bool:
        st: Set[int] = set()
        while True:
            if n == 1:
                return True

            if n in st:
                return False

            st.add(n)

            n = self.square_digits(self.get_digits(n))

    def get_digits(self, num: int):
        digits: List[int] = []
        while num:
            digits.append(num % 10)
            num = num // 10
        return digits

    def square_digits(self, digits: List[int]):
        sum = 0

        for digit in digits:
            sum += digit * digit

        return sum
