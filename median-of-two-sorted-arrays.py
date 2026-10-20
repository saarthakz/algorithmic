"""
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution should run in O(log(m+n)) time.
"""

from bisect import bisect_right


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return float(self.find_kth_by_value(nums1, nums2, (total + 1) // 2))
        else:
            left = self.find_kth_by_value(nums1, nums2, total // 2)
            right = self.find_kth_by_value(nums1, nums2, total // 2 + 1)
            return (left + right) / 2.0

    def find_kth_by_value(self, A: list[int], B: list[int], k: int) -> int:
        # Determine absolute value bounds across both arrays
        low = min(A[0] if A else float("inf"), B[0] if B else float("inf"))
        high = max(A[-1] if A else float("-inf"), B[-1] if B else float("-inf"))

        while low < high:
            mid = (low + high) // 2

            # Count total elements <= mid across both lists
            count = bisect_right(A, mid) + bisect_right(B, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return int(low)
