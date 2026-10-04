"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        operator = set(["+", "-", "*", "/"])

        for token in tokens:
            if token in operator:
                second = st.pop()
                first = st.pop()
                token = self.eval_expr(first, second, token)
            st.append(token)

        return float(st.pop()).__round__()

    def eval_expr(self, first_op_tok: str, second_op_tok: str, operator_tok: str):
        first = int(first_op_tok)
        second = int(second_op_tok)

        match operator_tok:
            case "+":
                return first + second
            case "-":
                return first - second
            case "*":
                return first * second
            case "/":
                return first / second
        return 1e10
