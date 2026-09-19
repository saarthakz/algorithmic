"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strPtr = 0
        endPtr = len(s) - 1

        while strPtr <= endPtr:
            fChar = s[strPtr]
            bChar = s[endPtr]

            # Skip non-alphanumeric characters from the front
            if not fChar.isalnum():
                strPtr += 1
                continue

            # Skip non-alphanumeric characters from the back
            if not bChar.isalnum():
                endPtr -= 1
                continue

            # Compare characters (case-insensitive)
            if fChar.lower() != bChar.lower():
                return False

            strPtr += 1
            endPtr -= 1

        return True
