"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""


class Solution:
    def isValid(self, st: str) -> bool:
        stack = []

        mapping = {"}": "{", "]": "[", ")": "("}

        openings = set(("(", "{", "["))

        for idx in range(len(st)):
            char = st[idx]

            # Opening character
            if char in openings:
                stack.append(char)

            # Closing character
            elif char in mapping:
                if len(stack) and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    # Underflow or mismatch
                    return False

        return len(stack) == 0
