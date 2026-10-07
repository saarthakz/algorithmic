"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day.

If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
"""

from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Val, Idx, Running Pop Count
        stack: List[List[int]] = [[temperatures[0], 0, 0]]

        ans = [0] * len(temperatures)

        for idx in range(1, len(temperatures)):
            curr = temperatures[idx]
            curr_pop_cnt = 0

            # Top value is stack[-1][0]
            while len(stack) and curr > stack[-1][0]:
                popped_val, popped_idx, pop_cnt = stack.pop()

                # Use the "top's" base value for elements underneath
                curr_pop_cnt += 1 + pop_cnt
                ans[popped_idx] = curr_pop_cnt

            # Update the pop count for the elements underneath so that they also are aware of the running index so far
            # We can update the entire stack, but instead we choose to update only the top element, and use that as a base value to be added to all the elements underneath
            if len(stack):
                stack[-1][2] += curr_pop_cnt

            # A fresh insert has no running pop count
            stack.append([curr, idx, 0])

        return ans
