from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = [0, 0]  # [countAhead, visited]

        def visit(num):
            """Returns the total count starting from num"""
            if num not in dic:
                return 0

            countAhead, visited = dic[num]

            if visited:
                # Already processed, return stored value + 1 (for this number)
                return countAhead + 1

            # Recursively get count from next number
            aheadCount = visit(num + 1)

            # Mark as visited and store how many numbers come after this
            dic[num] = [aheadCount, 1]

            # Return total count including this number
            return aheadCount + 1

        maxCount = 0
        for num in nums:
            if dic[num][1] == 0:  # If not visited
                maxCount = max(maxCount, visit(num))

        return maxCount
