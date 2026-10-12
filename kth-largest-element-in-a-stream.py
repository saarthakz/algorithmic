"""
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

    constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
    int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

"""

from typing import List
import bisect

# Acceptable solution but nums.insert is linear in time, and we need logarithmic
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        ins_idx = bisect.bisect(self.nums, val)
        self.nums.insert(ins_idx, val)
        return self.nums[-self.k]
"""

import heapq


# Optimal solution with Heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Heapify the list
        heapq.heapify(nums)

        # Make the heap with atmost 'k' elements
        while len(nums) > k:
            heapq.heappop(nums)

        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
