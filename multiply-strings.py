"""
You are given two strings num1 and num2 that represent non-negative integers.

Return the product of num1 and num2 in the form of a string.

Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

Note: You can not use any built-in library to convert the inputs directly into integers.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is zero, the product is zero
        if num1 == "0" or num2 == "0":
            return "0"

        num1_len, num2_len = len(num1), len(num2)

        # The product can have at most num1_len + num2_len digits
        result = [0] * (num1_len + num2_len)

        # Traverse num1 from right to left
        for idx in range(num1_len - 1, -1, -1):

            # Traverse num2 from right to left
            for _idx in range(num2_len - 1, -1, -1):

                # Convert individual characters into integer digits
                digit1 = ord(num1[idx]) - ord("0")
                digit2 = ord(num2[_idx]) - ord("0")

                # Multiply the digits and add the accumulated value
                # at the corresponding result position
                total = digit1 * digit2 + result[idx + _idx + 1]

                # Store the current digit
                result[idx + _idx + 1] = total % 10

                # Add the carry to the preceding position
                result[idx + _idx] += total // 10

        # Remove leading zeros from the result
        start_idx = 0
        while start_idx < len(result) and result[start_idx] == 0:
            start_idx += 1

        # Convert the result digits into a string
        return "".join(str(digit) for digit in result[start_idx:])
