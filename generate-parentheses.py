"""
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: List[str], open_count: int, close_count: int):

            # Base condition, 2 (pair) * n means we have reached a valid combination
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result
