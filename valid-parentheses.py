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
