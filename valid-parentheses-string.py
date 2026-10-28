"""
You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

    Every left parenthesis '(' must have a corresponding right parenthesis ')'.
    Every right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

"""


class Solution:
    def checkValidString(self, st: str) -> bool:

        return self.check(st, "(", ")") and self.check(st[::-1], ")", "(")

    def check(self, st: str, ob: str, cb: str):
        closing = 0
        opening = 0
        wildcard = 0

        for ch in st:
            if ch == cb:
                closing += 1
            elif ch == ob:
                opening += 1
            else:
                wildcard += 1

            if closing > opening + wildcard:
                return False

        return True
